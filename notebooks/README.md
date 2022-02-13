# Notebooks

## Architecture & Their Results

### LSTM
1. 1 LSTM & 1 Dense Layer
2. 2 LSTM & 1 Dense Layer
3. 1 LSTM & 2 Dense Layer
4. 1 Bidirectional LSTM & 1 Dense Layer
5. 1 Bidirectional LSTM & 2 Dense Layer

Epochs Trained on : 50
Dataset used to train the model : 
1. [Shakespeare's Play](https://www.kaggle.com/kingburrito666/shakespeare-plays)
2. [Light Novels](https://www.kaggle.com/utsavk02/4-light-novel-for-text-generation)

Results from the above LSTM Models :
```
maxlen set to 20
1.  Julius Xiao Che Was A Very Genius Step In His Heart And Caused The People Of The Xiao Clan To Be
2.  Thou Xiao Che Was A Very Genius Step In His Heart And Caused The People Of The Xiao Clan To Be
3.  King Is You Really I Brotherinlaw I Have Just I Do You Want To Die About You To Say That You Are
4.  Death Of Course Yun Che Had Already Ignored His Stance As Seriousness As His Entire Profound Veins He Had Always Been In
5.  The Princess Was A Large Disaster Of The Xiao Clan And The Other Of The Seven Sects Had Always Seen The Sects
6.  Thanos Xiao Che Was A Very Genius Step In His Heart And Caused The People Of The Xiao Clan To Be
```

### GPT2
1. Base GPT
2. GPT Fine Tuned

Epochs Fine Tuned on : 1000
Dataset used to train the model : 
1. [Light Novels](https://www.kaggle.com/utsavk02/4-light-novel-for-text-generation)

Results from the above GPT2 Models :
  1. Fine Tuned on Japanese Light Novel 
    <p>
    Story Beginning Words : Zombie Apocalypse
    Length : 300
    Zombie Apocalypse’s rank and level.“i’ll clean up the corpses, then! hurry up and come back tomorrow morning!”lan xueruo smiled as she said that. she instructed the disciples of the seven deadly sword pavilion to hurry up and come back tomorrow morning in the event of an emergency. “i also want to hurry up and come back tomorrow morning!” yun che immediately turned his back around and faced lan xueruo. lan xueruo had already placed all her profound strength into her right now, and her posture was completely silent; the only sound that could be heard from outside was the muffled sound of her footsteps. at the same time, the corners of yun che’s mouth curled up like a crescent. the expression in her eyes was extremely hazy; it was as if she had just wanted to say something, but couldn’t come up with it.“i’m afraid not, because this yun che is not like this after all.” lan xueruo shook her head. she knew that the first time he had confronted xiao luocheng, he’d definitely been completely crippled; although she couldn’t even see a trace of the emotion of anger and humiliation towards him, she was also extremely relieved.“haha, that’s great! you’re really the one that’s worried, right?” yun che said, not caring about what was on his mind anymore.“what’
    </p>



