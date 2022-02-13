# NovelAI

#### Note: This is a rough Readme , this Readme will be updated soon with all the details

## 📌 About
Light Novel Generation using LSTM & GPT-2. This Project was made in *KJSIEIT Code Odyssey Hackathon*


## 🎯 Key Features
* Text Generation Using GPT-2 

## 💻 Development Process
### Various Techniques/Models Used
* LSTM 
  * 1 LSTM & 1 Dense Layer
  * 2 LSTM & 1 Dense Layer
  * 1 LSTM & 2 Dense Layer
  * 1 Bidirectional LSTM & 1 Dense Layer
  * 1 Bidirectional LSTM & 2 Dense Layer 
* GPT2
  * Base
  * Fine Tuning 

### Datasets used
* [Light Novel Dataset](https://www.kaggle.com/utsavk02/4-light-novel-for-text-generation)
  * Contains 4 Light Novel :
    * Against the Gods
    * Level 999 Villager
    * The Dungeon Seeker
    * The Skeleton Knight
  * JK Rowling's Book :
    * Harry Potter 


### Notebooks
* [Text Generation using LSTM](https://github.com/utsavk28/NovelAI/blob/main/notebooks/text-generation-using-lstm.ipynb)
* [Text Generation using HuggingFace GPT2](https://github.com/utsavk28/NovelAI/blob/main/notebooks/text-generation-with-huggingface-gpt2.ipynb)
* [Fine Tuning GPT2 for Text Generation](https://github.com/utsavk28/NovelAI/blob/main/notebooks/text-generation-using-fine-tuned-gpt-2.ipynb)


## 🛠 Project Setup

1. Clone the repository using the ```git clone```
```
 $ git clone https://github.com/utsavk28/NovelAI.git
```
2. Create a virtual environment
```
 $ virtualenv venv
 $ source venv/bin/activate
```
3. Install the required packages
```
 $ pip install -r requirements.txt
```
4. Run the app
```bash
 $ cd webapp
 $ streamlit run main.py
```

## Group members
- [Utsav Khatu](https://github.com/utsavk28)


## 📸 Results
[Demo link](https://www.youtube.com/watch?v=gzyclx5nLB0g)
![HomePage](https://github.com/utsavk28/NovelAI/blob/main/images/NovelAI.png) 
![GeneratorPage](https://github.com/utsavk28/NovelAI/blob/main/images/NovelAI-Generator.png) 

## 🌐 Conclusion
