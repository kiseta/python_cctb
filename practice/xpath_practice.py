__author__ = 'tk'

# XPATH review

# Rule # 1 - there is alway the way to find an element, you just need to find it
# Rule #2 Use XPATH only if there is absolutely no other option
# Other locator strategies:
# 1 - ID - is the best, unless it's dynamic
# 2 - NAME - is second best, CLASS_NAME
# 3 - LINK_TEXT, PARTIAL_LINK_TEXT
# 4 - XPATH
# 5 - CSS Selector

# How to build a correct (professional, good-looking, portfolio worthy) XPATH
# start with the tag nearest to the element to find
# Example:
# HTML Code:
# <a href="../user/view.php?id=1815&amp;course=1" id="id_normalID">John Smith</a>
# XPATH copied from the browser (strongly not recommended, flakey, unreliable and non-professional looking)
# /html/body/div[2]/div[4]/div/div//span/section/div/div[1]/table/tbody/tr[7]/td[1]/a

# RECOMMENDED XPATH STRATEGY:
# xpath = '//a[]'
# xpath = '//a[contains()]'
# xpath = '//a[contains(.,"")]'
# . is replaced by text()
# text to find goes inside the quotes
# xpath = '//a[contains(text(),"John Smith")]'
# other alternatives:
# xpath1 = '//a[text()="John Smith"]'
# xpath2 = '//a[contains(.,"John Smith")]'
# xpath3  = '/*[contains(.,"John Smith")]'
# * means any element
# . means any attribute

# Two sources of XPATH data
# source 1: text between the opening and closing html tags (nested tags)
# <a ....>John Smith</a>
# <div ....><h3>Welcome to our website</h3></div>
# <span ...><a ....>John Smith</a></span>
# <td><span ...><a ....>John Smith</a></span></td>

# <table>
# <tr><td>Row 1 Col 1</td><td>Row 1 Col 2</td><<td>Row 1 Col 3</td>/tr>
# <tr><td>Row 2 Col 1</td><td>Row 2 Col 2</td><<td>Row 2 Col 3</td>/tr>
# </table>

# HTML Code:
# <a href="../user/view.php?id=1815&amp;course=1" id="id_normalID">John Smith</a>

# source # 2: attributes inside opening tag
# xpath4 = '//a[contains(@href, "id=1815")]'
# xpath5 = '//a[contains(@id, "id_normalID")]'
