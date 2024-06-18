#super string - count of each string == ascii value
# ascii value , a=1, b=2
st=input()
for i in st:
     d=ord(i)+1-ord('a')
     print(d)
     if st.count(i)!=d:
          print("not a super string")
          break
else:
     print("super string")
