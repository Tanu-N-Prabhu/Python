# import the additional module
import difflib
import re

# define original text
text1 = '1. UNC SSO details 2. Intergation with Connect Carolina (Classes System), need details 3. Must follow Carolina Together style guide, need details 4. How the ML model will be integrated into Admin panel. Will then provide REST APIs for that? or we need to integrate the ML model into back end system? 5. Need front end all API details 6. explain "Stay" and "Exit" 7. '
text2 = '1. UNC SSO details 2. Intergation with disconnect Carolina (Classes System), need details 3. Must follow Carolina alone style guide, need details 4. How the ML model will be integrated into Admin panel. Will then provide REST APIs for that? or we do not need to integrate the ML model into back end system? 5. do not Need front end all API details 6. explain "Stay" and "Exit"'

original = re.split("\s+", text1)
edited = re.split("\s+", text2)

# original = ["About the IIS", "", "IIS 8.5 has several improvements related",
#             "to performance in large-scale scenarios, such",
#             "as those used by commercial hosting providers and Microsoft's", "own cloud offerings."]
# 
# # define modified text
# edited = ["About the IIS", "", "It has several improvements related", "to performance in large-scale scenarios."]

# initiate the Differ object
d = difflib.Differ()

# calculate the difference between the two texts
diff = d.compare(original, edited)

# output the result
print('\n'.join(diff))
