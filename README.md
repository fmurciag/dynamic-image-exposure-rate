# dynamic-image-exposure-rate
Dynamic adjustment of image exposure rate with tracking bar using the the gamma function

## Explain

As can be seen in the graph of the gamma function, when R>1, the curve is below R=1 and the value of the color space decreases, making the image less bright.

When 0<R<1, the curve is above R=1 and the value of the color space increases. Macroscopic performance is the increase in image brightness

<img src="source/grafico.png">

## Results 
<table>
  <tr>
    <td>R=0,48</td>
    <td>R=1</td>
    <td>R=2,11</td>
    <td>R=5,83</td>
  </tr>
  <tr>
    <td><img src="source/img1.png"></td>
    <td><img src="img_in/B3.jpg" width="75%" height="75%"></td>
    <td><img src="source/img2.png"></td>
    <td><img src="source/img4.png"></td>
  </tr>
 </table>
 
 ## How to use
 In the top you can see a track bar, the value of the track bar is R/0,01
 | R | Track bar     | 
| :-------- | :------- | 
| 1 | 100 |
| 0,5 | 50 |
| 1,5 | 150 |

 <img src="source/img2.png">
