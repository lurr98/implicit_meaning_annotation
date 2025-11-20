import re
import streamlit as st
from core.scripts.utils import display_progress, read_json_from_file, load_annotation, TASK_INFO

def remove_punctuation(text: str) -> str:

    text = " ".join(text.split("\n"))
    # remove listed numbers
    subbed_text = re.sub(r"\d\.", "", text)
    # remove URLs
    sub_subbed_text = re.sub(r"http[s]?://\S+|www\.\S+|<a href.+</a>", "<URL>", subbed_text)
    return re.sub(r"[”#*\+/<=>\[\]\\^_`{|}~]", "", sub_subbed_text)


def format_sample(question: dict) -> None:

    def labeled_paragraph(label, text, font_size="16px", font_weight="normal", indent="45"):
        st.markdown(
            f"""
            <div style="margin-left: 0; padding-left: {indent}px; text-indent: -{indent}px; font-size: {font_size}; font-weight: {font_weight}">
                <span style="background-color: rgba(210, 215, 225, 0.32); color: inherit; padding: 2px 4px; border-radius: 4px;">
                    {label}
                </span>
                {text}
            </div>
            """,
            unsafe_allow_html=True
        )

    # sentence 1 and 2 are switched bc we decided to put the revision first
    match = re.findall(r"<(.*)>", question["sentence_2"])
    blue_background = re.sub(r"<.*>", f":blue-background[{match[0]}]", question["sentence_2"])

    st.markdown(f":grey-background[*Article name:*] &emsp;{question["article_name"]}")
    st.markdown("")
    st.markdown(":grey-background[Read the following text and focus on the **bold sentence**.]")
    st.markdown(f"> {remove_punctuation(question["context_before"])}  \n> **{question["sentence_1"]}**  \n> {remove_punctuation(question["context_after"])}")
    st.markdown("")
    st.markdown("")
    st.markdown(":grey-background[Now read the modified text:]")
    st.markdown(f"> {remove_punctuation(question["context_before"])}  \n> **{blue_background}**  \n> {remove_punctuation(question["context_after"])}")
    st.markdown("")
    st.markdown(":grey-background[Does changing the bold sentence affect your understanding of the text?]")

    
def check_all_checkboxes(implicit: str, checkboxes: list, comment: str) -> bool:

    if implicit == "Yes":
        return True
    elif implicit == "No" and checkboxes[-1]:
        if comment:
            return True
    elif implicit == "No" and len([box for box in checkboxes[:-1] if box]) >= 1:
        return True
    else:
        return False


def print_annotation_schema(index: int, subtask: str="annotation") -> tuple[dict, str, list, str, str, bool]:
    """
    Prints the annotation schema that is seen on the qualification and annotation page.

    :param subtask: qualification or annotation
    :param index: The number sample to show
    :return: The sentence and widget inputs in the order they are displayed to the user.
    """
    if subtask == "qualification":
        samples = read_json_from_file(TASK_INFO["implicit_meaning_task"]["qualification_filepath"])
    else:
        samples = read_json_from_file(TASK_INFO["implicit_meaning_task"]["annotation_filepath"])

    # load values previously filled in checkboxes or None if this is first time annotating this sample
    sample_preload = load_annotation(subtask, index)
    if sample_preload is None:
        implicit_val, context_val, reasoning_val, complement_val, instruction_val, other_val = None, None, None, None, None, None
        comment_implicit_val, comment_not_implicit_val = "", ""
    else:
        implicit_val, context_val, reasoning_val, complement_val, instruction_val, other_val = (sample_preload["implicit_meaning"], 
                                                                                                sample_preload["if_implicit"][0], 
                                                                                                sample_preload["if_implicit"][1], 
                                                                                                sample_preload["if_implicit"][2], 
                                                                                                sample_preload["if_implicit"][3], 
                                                                                                sample_preload["if_implicit"][4]
                                                                                                )
        comment_implicit_val, comment_not_implicit_val = (sample_preload["comment_implicit"], sample_preload["comment_not_implicit"])

    question = samples[str(index)]
    # # display the "Sample 1/5" thing
    display_progress(key=subtask)

    format_sample(question)

    context, reasoning, complement, instruction, other = False, False, False, False, False
    comment_implicit, comment_not_implicit = "", ""
    # implicit = st.radio(
    #     ":grey-background[Does the first sentence implicitely convey the same meaning as the second one?]",
    #     ["Yes", "No"],
    #     key="implicit",
    #     horizontal=True,
    #     index=None,)

    col1, col2 = st.columns(2)
    with col1:
        implicit = st.segmented_control("", ["Yes", "No"], key=10 * index + 1, default=implicit_val)
        # col1, col2 = st.columns(2)
        # with col1:
        #     implicit = st.checkbox(key=10 * index + 1, label="Yes", value=None)
        # with col2:
        #     not_implicit = st.checkbox(key=10 * index + 2, label="No", value=None) 
        if implicit == "No":
            st.markdown("Please specify one or multiple reasons for your choice:")

            col3, col4 = st.columns(2)

            with col3:
                context = st.checkbox(key=10 * index + 2, label="Context", value=context_val, help="The added information is recoverable from the context.")
                reasoning = st.checkbox(key=10 * index + 3, label="Logical Reasoning", value=reasoning_val, help="The added information is a logical premise or consequence given some mutual knowledge that the author can expect from the reader.")
                complement = st.checkbox(key=10 * index + 4, label="Expected Information", value=complement_val, help="The type of information that was added is usually expected by the reader for the specific verb.")
                instruction = st.checkbox(key=10 * index + 5, label="Recoverable Instruction", value=instruction_val, help="The same action could be performed from both instructions.")

            with col4:
                other = st.checkbox("Other", value=other_val)
                comment_implicit = st.text_input(key=10 * index + 6, label="If applicable, specify other reasons that led to your decision:", value=comment_implicit_val, max_chars=200)
                if comment_implicit:
                    st.write(r"$\textsf{\scriptsize Thanks for your input!}$")
        else:
            comment_not_implicit = st.text_input(key=10 * index + 7, label="If you are unsure, select \"Yes\" and explain your thoughts here:", value=comment_not_implicit_val, max_chars=200)
            if comment_not_implicit:
                st.write(r"$\textsf{\scriptsize Thanks for your input!}$")

        checkboxes = [context, reasoning, complement, instruction, other]
        if check_all_checkboxes(implicit, checkboxes, comment_implicit):
            next_input = st.button(key = 10 * index + 8, label="Next", help="Save this annotation and advance to the next one.")
        else:
            next_input = None
    with col2:
        # add confidence score
        st.markdown("### Confidence Score")
        confidence = st.slider(
            label="How confident are you about your annotation?\n\n1 = Not confident at all, 5 = Very confident",
            min_value=1,
            max_value=5,
            value=3,
            step=1,
            key=10 * index + 10,
            help="1 = Not confident at all, 5 = Very confident"
        )

    return question, implicit, checkboxes, comment_implicit, comment_not_implicit, confidence, next_input