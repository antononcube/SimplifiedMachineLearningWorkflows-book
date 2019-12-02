# Wolfram U Quantlie Regression workflows lectures

## In brief

The lectures were recorded through Wolfram University (Wolfram U) in August-November 2019.

The lectures were recorded as Twitch sessions. The recordings can be found on both 
Twitch and 
[YouTube](https://www.youtube.com/playlist?list=PLxn-kpJHbPx17-6A5-yi2IbDZ0R9dFNHS).

The notebooks can be found here and in this
[Community](https://community.wolfram.com)
page: 
["[LiVE] Quantile Regression Workflows (WL Live-Stream Series)"](https://community.wolfram.com/groups/-/m/t/1787896).


## The live-coding sessions

(*It seems to be a good idea to start with the last, 5th lecture that gives Quantile Regression overview 
through questions and answers.)*

1. In the first 
[live-streaming / live-coding session](https://www.twitch.tv/wolfram/video/473572589) 
I demonstrated how to make 
[Quantile Regression](https://en.wikipedia.org/wiki/Quantile_regression)
workflows using the [software monad `QRMon`](https://community.wolfram.com/groups/-/m/t/1395719) 
and some of the underlying software design principles. (Namely 
["monadic programming"](https://community.wolfram.com/groups/-/m/t/1126923).)

2. In the [follow up live-coding session](https://www.twitch.tv/videos/481009848) I discussed topics like outliers removal (data cleaning), anomaly detection, and [structural breaks](https://en.wikipedia.org/wiki/Structural_break).

3. In the [third live-coding session](https://www.twitch.tv/videos/485939037):

   - First, I demonstrated and explained how to do QR-based time series simulations and their applications in Operations Research.
   - Next, I discussed QR in 2D and 3D and a related application.
  
4. In the [fourth live-coding session](https://www.twitch.tv/videos/498468049) I discussed the following the topics.

   - Review of previous sessions.
   - Proclaiming the upcoming `ResourceFunction["QuantileRegression"]`.
   - Predict tomorrow from today's data.
   - Using NLP techniques on time series.
   - Generation of QR workflows with natural language commands.
   
5. In the final, [fifth live-coding session](https://www.twitch.tv/videos/511900723) different questions were answered.
   Here is the list:

   - Can we apply Quantile Regression (QR) without the package QRMon?
      - Yes, see the Wolfram Functions Repository item “QuantileRegression”.
   - Are you computing QR using a moving window?
      - Related, how QR compares to Local regression? Or LOESS?
   - What do you do when the QR fitted curves (regression quantiles) intersect? 
   - How does QR fitted curve looks like over 3 points?
   - What approximation to pick for reconstructing the conditional CDF’s?
   - Why use QR? Is it just for better visualization of the signal?
   - What is the point of using those anomaly detection methods -- a human can easily do it?
   - Can we use Neural Networks instead of QR?
   - Are there implementations in other popular DS languages?


## Resource function

Instead of the software monad `QRMon` used in this book and the live-coding sessions the Wolfram Resource Function
[`QuantileRegression`](https://resources.wolframcloud.com/FunctionRepository/resources/QuantileRegression)
can be used. The resource page has many example applications that are also discussed in the live-coding sessions.