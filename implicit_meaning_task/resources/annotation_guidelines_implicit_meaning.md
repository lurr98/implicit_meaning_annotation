# Annotation Guidelines: Implicit Meaning

The goal of this annotation task is to find sentence pairs where one sentence contains **implicit meaning** that is made explicit in the other. More specifically, this means that, even though not everything is stated explicitly in the second sentence, both sentences convey **the same meaning** within the surrounding context.

For every item you will be shown two almost equivalent sentences, S1 and S2. However, the first sentence contains an additional element, marked in :blue-background[blue]. Do not worry about other changes in the sentence.

The sentences were taken from two versions of the same wikiHow article, so you will also be shown the preceding and succeeding context as well as the name of the corresponding wikiHow article.

Below you will find two buttons (:grey-background[Yes] and :grey-background[No]) as well as a comment section.

If you check the :grey-background[Yes] button, five more checkboxes and a different comment section will appear. You can check out this mini example here and play around with it:

---

##### :grey-background[**S1:**] Check the box below :blue-background[by clicking on it].
##### :grey-background[**S2:**] Check the box below.  

:grey-background[*Article name:*] &emsp;How_To_Annotate_This_Task.txt

:grey-background[*Context before:*] &nbsp;This is how the annotation task will look like. 

:grey-background[*Context after:*] &emsp;When you have ticked the box, five more checkboxes and a comment section will appear.
==SPLIT==

---

During the annotation task, select "Yes" if you think that the two sentences convey the same meaning in the given context, even though the second one does not state all information explicitly. If you do this, please specify the reason for your decision by ticking the relevant checkboxes among the ones that will appear. You can choose from the following categories:

---

### ✔️ Positive Indicators – Implicit Meaning

#### **1. Context**
The omitted information is recoverable from the context (including the article title). In the following example, the reference “doll” can be inferred from the title of the article.

**Example:**  
*How_To_Care_for_an_Uglydoll.txt*  
- **Sentence 1:** Look at the tag :blue-background[of the doll].
- **Sentence 2:** Look at the tag.  

---

#### **2. Logical Reasoning**
The omitted information is a logical premise or consequence given some mutual knowledge that the author can expect from the reader. In the following example, the author can expect the reader to know that you do not have to buy something if you already possess it.

**Example:**  
*How_To_Shorten_a_Bike_Chain.txt*  
- **Sentence 1:** Purchase a universal chain tool :blue-background[if you don’t have one].
- **Sentence 2:** Purchase a universal chain tool.  

---

#### **3. Expected Information**

The type of information (e.g. a reason, consequence, location) that was omitted is usually expected by the reader for the specific verb. For instance, it is typical to mention the reason for surprise, however, it is possible to omit it, as the next example shows.

**Example:**  
*How_To_Pack_for_a_Day_Trip.txt*  
- **Sentence 1:** Bring more than you expect to eat, you'll be surprised :blue-background[how hungry you may get].
- **Sentence 2:** Bring more than you expect to eat, you might be surprised.  

---

#### **4. Recoverable Instruction**
The instruction remains interpretable even when the information is omitted such that the same action would be performed from both instructions. In the following example, it is clear that the leg-raising should be performed while in the hip bridge position.

**Example:**  
*How_To_Do_Leg_Exercises.txt*  
- **Sentence 1:** There are variations of the hip bridge such as raising one leg :blue-background[while in the bridge position].
- **Sentence 2:** There are variations of the hip bridge such as raising one leg.  

---

**Note:**  
A sentence pair may match multiple categories.  

[comment]: # (For example, the third sentence could also fall under **Context**, since what one might be surprised about is evident from the immediate context.)

If you think the added information is implicit meaning but **none of the positive criteria** apply, please tick the **Other** checkbox and explain your reasoning in the comment section next to it.

---

### ❌ Negative Indicators — Not Implicit Meaning

If any of the following apply, select "No". These suggest **new information** rather than implicit content:

#### **1. Omission changes the core meaning**
The omission fundamentally changes the meaning of the original sentence.

**Example:**  
*How_To_Calculate_Z_Scores.txt*  
- **Sentence 1:** :blue-background[Subtract each sample from] the sample mean.
- **Sentence 2:** Find the sample mean.  

---

#### **2. Omitted information is too specific**
The omitted information introduces specific entities, concepts or events that a regular reader cannot be expected to know about.

**Example:**  
*How_To_Put_Game_Saves_on_Your_PSP.txt*  
- **Sentence 1:** Don't forget to remove the cable :blue-background[by Kenneth Arthur].
- **Sentence 2:** Don't forget to remove the cable.  

---

If you are unsure about whether the omitted information is implicit meaning, select "No" and write a comment in the comment section below it.
