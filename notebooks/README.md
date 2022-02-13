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


Best LSTM Model :
```
  1 Bidirectional LSTM & 1 Dense Layer
```

Best Results from the above LSTM Models :
```
maxlen set to 20
1.  Julius Xiao Che Was A Very Genius Step In His Heart And Caused The People Of The Xiao Clan To Be
2.  Thou Xiao Che Was A Very Genius Step In His Heart And Caused The People Of The Xiao Clan To Be
3.  King Is You Really I Brotherinlaw I Have Just I Do You Want To Die About You To Say That You Are
4.  Death Of Course Yun Che Had Already Ignored His Stance As Seriousness As His Entire Profound Veins He Had Always Been In
5.  The Princess Was A Large Disaster Of The Xiao Clan And The Other Of The Seven Sects Had Always Seen The Sects
6.  Thanos Xiao Che Was A Very Genius Step In His Heart And Caused The People Of The Xiao Clan To Be
```
