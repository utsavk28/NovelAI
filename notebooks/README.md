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
    Story Beginning Words : Zombie Apocalypse<br/>
    Length : 300<br/>
    Zombie Apocalypse’s rank and level.“i’ll clean up the corpses, then! hurry up and come back tomorrow morning!”lan xueruo smiled as she said that. she instructed the disciples of the seven deadly sword pavilion to hurry up and come back tomorrow morning in the event of an emergency. “i also want to hurry up and come back tomorrow morning!” yun che immediately turned his back around and faced lan xueruo. lan xueruo had already placed all her profound strength into her right now, and her posture was completely silent; the only sound that could be heard from outside was the muffled sound of her footsteps. at the same time, the corners of yun che’s mouth curled up like a crescent. the expression in her eyes was extremely hazy; it was as if she had just wanted to say something, but couldn’t come up with it.“i’m afraid not, because this yun che is not like this after all.” lan xueruo shook her head. she knew that the first time he had confronted xiao luocheng, he’d definitely been completely crippled; although she couldn’t even see a trace of the emotion of anger and humiliation towards him, she was also extremely relieved.“haha, that’s great! you’re really the one that’s worried, right?” yun che said, not caring about what was on his mind anymore.“what’
    </p>
  2. Fine Tuned on Harry Potter
    <p background-color: var(--color-canvas-subtle) > 
    Story Beginning Words :The Most Dangerous Spell<br/>
    Length : 300<br/>
    The Most Dangerous Spell!”possible explanation.the fact that the spell had already been cast and the effects had been negated caused the most apprehension within the palace. this was probably the most dangerous spell that the seven sects combined.they originally had planned to use this spell to stop the demon king’s army, so this was indeed the most dangerous spell that they could use.not only that, this was the most dangerous spell that evil could use.the profound sky continent’s number one ranked sky profound realm’s protective profound arts was the sky poison pearl’s stormy secret arts.so it was not just the sky poison pearl but the sky poison pearl’s stormy secret arts that could protect the evil god’s profound energy.the sky poison pearl used to protect its profound energy had been wiped clean for obvious reasons.the profound sky continent’s number one ranked sky profound realm’s protective profound arts was the sky poison pearl’s stormy secret arts.this was the most dangerous profound arts.the sky poison pearl’s stormy secret arts had an area of effect smaller than the uiria’s storm of fire, but it could be said that it was the most dangerous profound art. the reason why it was used was because the sky poison pearl’s stormy secret arts blocked most of the evil god’s secret arts’ negative side effects.the stormy secret arts that had negative side effects were those that would cause suffering or death.there was a reason why the heavenly knight’s
    </p>




