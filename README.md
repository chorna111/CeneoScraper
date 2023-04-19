# CeneoScraper
## Selektory css składowych opinii w serwisie Ceneo.pl
| Składowa | nazwa | Selector |
| --- | --- | --- |
| Opinia| Opinion | div.js\_product-review |
| Id opinii | Opinion\_id | ['data-entry-id'] |
| Autor | Author | span.user-post\_\_author-recommendation |
| Rekomendacja | Recommendation | span.user-post\_\_author-recommendation\>em |
| Liczba gwiazdek | Score | span.user-post\_\_score |
| Czy opinia potwierdzona zakupem | Purchased | div.review-pz |
| Data wystawienia opinii | Published\_at | span.user-post\_\_published\>time:nth-child(1)['datetime'] |
| Data zakupu produktu | Purchased\_at | span.user-post\_\_published\>time:nth-child(2)['datetime'] |
| Ile osób uznało opinię za przydatną | Thumbs\_up | span[id^=votes-yes;button.vote-yes['data-total-vote'];button.vote-yes\>span|
| Ile osób uznało osób za nieprzydatną | Thumbs\_down | span[id^=votes-no;button.vote-no['data-total-vote'];button.vote-no\>span|
| Treść opinii | Content | div.user-post\_\_text |
| Lista wad | Cons | div.review-feature\_\_col:has(\>div. review-feature\_\_title--negatives)\>div.review-feature\_\_item |
| Lista zalet | Pros | div.review-feature\_\_col: has(\>div. review-feature\_\_title--positives)\> div.review-feature\_\_item |
## Uzyte biblioteki
### -Requests
### -BeautifulSoup4
###-Pandas
###-Matplotlib
