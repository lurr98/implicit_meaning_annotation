# Annotation Guidelines: Implicit Meaning

The goal of this annotation task is to find sentence pairs where one sentence contains **implicit meaning** that is made explicit in the other. More specifically, this means that, even though not everything is stated explicitly in the second sentence, both sentences convey **the same meaning** within the surrounding context.

For every item you will first be shown the name of the article from which the following sentences were taken. Below that you will find two almost equivalent texts where one sentence is highlighted in bold. The bold sentence in the first text contains an additional element, marked in :blue-background[blue]. Do not worry about other changes in the sentence.

Below the texts you will find two buttons (:grey-background[Yes] and :grey-background[No]) as well as a comment section.

If you check the :grey-background[Yes] button, five more checkboxes and a different comment section will appear. You can check out this mini example here and play around with it:

---
:grey-background[*Article name:*] &emsp;How_To_Annotate_This_Task.txt

Read the following text and focus on the **bold sentence**. 
 

> This is how the annotation task will look like. 
> **Check the box below :blue-background[by clicking on it].** 
> When you have ticked the box, five more checkboxes and a comment section will appear. 
 
\
:grey-background[Now read the modified text which omits the highlighted part:] 
 

> This is how the annotation task will look like. 
> **Check the box below.** 
> When you have ticked the box, five more checkboxes and a comment section will appear.  
 
\
:grey-background[Do you understand both of the texts in the same way?]

==SPLIT==

---

During the annotation task, select "Yes" if you think that the two sentences convey the same meaning in the given context, even though the second one does not state all information explicitly. If you do this, please specify the reason for your decision by ticking the relevant checkboxes among the ones that will appear. You can choose from the following categories:

---

### ✔️ Positive Indicators – Implicit Meaning

#### **1. Context**
The omitted information is recoverable from the context (including the article title). In the following example, the reference “doll” can be inferred from the title of the article.

**Example:**  
*How_To_Care_for_an_Uglydoll.txt*  
* When you buy it, it has a tag with its name and its personality.  
  **Look at the tag :blue-background[of the doll].**  
  Now you know what it likes so far.

* When you buy it, it has a tag with its name and its personality.  
  **Look at the tag.**  
  Now you know what it likes so far.

---

#### **2. Logical Reasoning**
The omitted information is a logical premise or consequence given some mutual knowledge that the author can expect from the reader. In the following example, the author can expect the reader to know that you do not have to buy something if you already possess it.

**Example:**  
*How_To_Shorten_a_Bike_Chain.txt*  
* **Purchase a universal chain tool :blue-background[if you don’t have one].**  
  This tool pushes the pins out of your chain to allow link removal.

* **Purchase a universal chain tool.**  
  This tool pushes the pins out of your chain to allow link removal.

---

#### **3. Expected Information**

The type of information (e.g. a reason, consequence, location) that was omitted is usually expected by the reader for the specific verb. For instance, it is typical to mention the reason for surprise, however, it is possible to omit it, as the next example shows.

**Example:**  
*How_To_Pack_for_a_Day_Trip.txt*  
* If it's cold, or in high altitude, bring a thermos with some soup. One of the best warm, light, and portable meals possible.  
  **Bring more than you expect to eat, you'll be surprised :blue-background[how hungry you may get].**

* If it's cold, or in high altitude, bring a thermos with some soup. One of the best warm, light, and portable meals possible.  
  **Bring more than you expect to eat, you might be surprised.**

---

#### **4. Recoverable Instruction**
The instruction remains interpretable even when the information is omitted such that the same action would be performed from both instructions. In the following example, it is clear that the leg-raising should be performed while in the hip bridge position.

**Example:**  
*How_To_Do_Leg_Exercises.txt*  
* This move will target your glutes and upper thighs.  
  **There are variations of the hip bridge such as raising one leg :blue-background[while in the bridge position].**  
  Lie down on your back with your knees bent and facing upward.

* This move will target your glutes and upper thighs.  **There are variations of the hip bridge such as raising one leg.** 
  Lie down on your back with your knees bent and facing upward.

---

**Note:**  
A sentence pair may match multiple categories.  

[comment]: # (For example, the third example could also fall under **Context**, since what one might be surprised about is evident from the immediate context.)

If you think the added information is implicit meaning but **none of the positive criteria** apply, please tick the **Other** checkbox and explain your reasoning in the comment section next to it.

---

### ❌ Negative Indicators — Not Implicit Meaning

If any of the following apply, select "No". These suggest **new information** rather than implicit content:

#### **1. Omission changes the core meaning**
The omission fundamentally changes the meaning of the original sentence.

**Example:**  
*How_To_Calculate_Z_Scores.txt*  
* **:blue-background[Subtract each sample from] the sample mean.**  
  Add together the values of all of the samples.

* **Find the sample mean.**  
  Add together the values of all of the samples.

---

#### **2. Omitted information is too specific**
The omitted information introduces specific entities, concepts or events that a regular reader cannot be expected to know about.

**Example:**  
*How_To_Put_Game_Saves_on_Your_PSP.txt*  
* Put the game in that you got the save data from and see if it works.  
  **Don't forget to remove the cable :blue-background[by Kenneth Arthur].**

* Put the game in that you got the save data from and see if it works. 
  **Don't forget to remove the cable.**

---

If you are unsure about whether the omitted information is implicit meaning, select "No" and write a comment in the comment section below it.
