with open("state_info.csv", "r") as state_info_file:
	state_info = state_info_file.read().split("\n")

for index, state  in enumerate(state_info):
	state_info[index] = state.split(",")

#print state_info
a = ""

for state in state_info:
	state_count = int(state[0])
	a += """<table border="1">\n<tr>\n<td colspan="2"> {0} </td>\n</tr>
<tr>\n<td> Rank: {1} </td>\n<td> Percent: {2}% </td>\n</tr>
<tr>\n<td> US House Members: {3} </td>\n<td> Population: {4} </td>
</tr>\n</table>""".format([1][1], state_info[1][0], state_info[1][4], state_info[1][3], state_info[1][2])

print a

with open("state_info.html", "w") as state_info_html:
	state_info_html_details = state_info_html.write(a)
# Challenge 3: Using state_info.csv, create an HTML page that has a table for *each* state with all of the state details.

# Sample output:

# <table border="1">
# <tr>
# <td colspan="2"> California </td>
# </tr>
# <tr>
# <td> Rank: 1 </td>
# <td> Percent: 11.91% </td>
# </tr>
# <tr>
# <td> US House Members: 53 </td>
# <td> Population: 38,332,521 </td>
# </tr>
# </table>

# Challenge 4 (Not a Python challenge, but an HTML/Javascript challenge): When you make a choice from the drop-down menu, jump to that state's table.