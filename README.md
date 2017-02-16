# Hong Kong public library searcher
A small script designed to search public library books in bulk

I built this because of 好書龍虎榜. It is hard to search for books 60 books at once. Therefore this is written in order to finish that.

# Usage
1. Install Python and pipenv
2. Install dependencies by running `pipenv install`
3. Run main.py
4. Use result printed on screen. Go to library and borrow it.

# Change search library
By default, Tiu King Leng library will be searched.

You may get a list of library ID by executing `python ls-library.py`.
The script will print out name of library to library ID on screen.

A list of library is also available in [below section](#library-id).

Set environment variable, `LIBRARY_LOCATION` to the ID of your desired library to change search location.

For example, if I would like to search for Central library, execute the following:

```bash
LIBRARY_LOCATION='1000000' python main.py
```

This will print a list of available books in central library.

# Book list
The book list included is the 28th of 好書龍虎榜, reading report done in 2016-2017 academic year.

To update the list, enter ISBN of the books into `books` file.

# Library ID
01. 香港仔公共圖書館 - 501000000
02. 鴨脷洲公共圖書館 - 701000000
03. 蝴蝶邨公共圖書館 - 702000000
04. 柴灣公共圖書館 - 502000000
05. 長洲公共圖書館 - 503000000
06. 大會堂公共圖書館 - 301000000
07. 電氣道公共圖書館 - 703000000
08. 花園街公共圖書館 - 504000000
09. 粉嶺公共圖書館 - 505000000
10. 粉嶺南公共圖書館 - 904340000
11. 富山公共圖書館 - 704000000
12. 香港中央圖書館 - 1000000
12. 香港中央圖書館(藝術資源中心) - 904090000
13. 紅磡公共圖書館 - 705000000
14. 九龍公共圖書館 - 302000000
15. 九龍城公共圖書館 - 706000000
16. 荔枝角公共圖書館 - 506000000
17. 藍田公共圖書館 - 707000000
18. 鯉魚門公共圖書館 - 708000000
19. 瀝源公共圖書館 - 709000000
20. 駱克道公共圖書館 - 507000000
21. 樂富公共圖書館 - 710000000
22. 龍興公共圖書館 - 711000000
23. 馬鞍山公共圖書館 - 508000000
24. 梅窩公共圖書館 - 712000000
25. 牛池灣公共圖書館 - 509000000
26. 牛頭角公共圖書館 - 510000000
27. 北葵涌公共圖書館 - 511000000
28. 南丫島北段公共圖書館 - 713000000
29. 北角公共圖書館 - 512000000
30. 坪洲公共圖書館 - 715000000
31. 屏山天水圍公共圖書館 - 904220000
32. 保安道公共圖書館 - 513000000
33. 薄扶林公共圖書館 - 716000000
34. 鰂魚涌公共圖書館 - 514000000
35. 西貢公共圖書館 - 515000000
36. 新蒲崗公共圖書館 - 516000000
37. 秀茂坪公共圖書館 - 717000000
38. 沙頭角公共圖書館 - 718000000
39. 沙田公共圖書館 - 303000000
40. 石硤尾公共圖書館 - 714000000
41. 石塘咀公共圖書館 - 517000000
42. 石圍角公共圖書館 - 719000000
43. 上水公共圖書館 - 518000000
44. 瑞和街公共圖書館 - 519000000
45. 順利邨公共圖書館 - 720000000
46. 小西灣公共圖書館 - 904170000
47. 士美非路公共圖書館 - 721000000
48. 南葵涌公共圖書館 - 520000000
49. 南丫島南段公共圖書館 - 722000000
50. 赤柱公共圖書館 - 723000000
51. 大興公共圖書館 - 521000000
52. 大角咀公共圖書館 - 724000000
53. 大澳公共圖書館 - 725000000
54. 大埔公共圖書館 - 522000000
55. 天水圍北公共圖書館 - 726000000
56. 調景嶺公共圖書館 - 904200000
57. 土瓜灣公共圖書館 - 524000000
58. 將軍澳公共圖書館 - 525000000
59. 尖沙咀公共圖書館 - 727000000
60. 青衣公共圖書館 - 526000000
61. 荃灣公共圖書館 - 304000000
62. 慈雲山公共圖書館 - 728000000
63. 屯門公共圖書館 - 305000000
64. 東涌公共圖書館 - 729000000
65. 元州街公共圖書館 - 730000000
66. 黃泥涌公共圖書館 - 731000000
67. 油蔴地公共圖書館 - 527000000
68. 耀東公共圖書館 - 732000000
69. 元朗公共圖書館 - 528000000
70. 流動圖書館一 - 901000000
71. 流動圖書館二 - 902000000
72. 流動圖書館三/十 - 903000000
73. 流動圖書館四 - 904000000
74. 流動圖書館五 - 901020000
75. 流動圖書館六/九 - 904040000
76. 流動圖書館七 - 904050000
77. 流動圖書館八 - 904060000
78. 流動圖書館十一 - 904310000
79. 流動圖書館十二 - 904320000
