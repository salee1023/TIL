git branch feature/nav

git switch feature/nav

git add .

git commit -m "add header"

---

git branch feature/footer

git switch feature/footer

git add .

git commit -m "add footer"

![image-20201016105850056](git%20branch%20featurenav.assets/image-20201016105850056.png)

---

git push origin feature/nav

git push origin feature/footer

`머지리퀘스트` 버튼클릭, 충돌이 없으면 `remove source branch` 버튼 클릭하고 `merge`

![image-20201016110814679](git%20branch%20featurenav.assets/image-20201016110814679.png)

---

git switch master

git pull origin master

git branch -d feature/nav

git log --oneline



git switch master

git pull origin master

git branch -d feature/footer

git log --oneline

----

**<충돌 발생했을 때>**

git branch feature/title

git switch feature/title

git add .

git commit -m "update titile name en"

git push origin feature/title



git branch feature/title-ko

git switch feature/title-ko

git add .

git commit -m "update titile name ko"

git push origin feature/title-ko



`충돌 해결` 버튼 클릭 후 merge



git switch master

git pull origin master

git branch -d feature/title



git switch master

git pull origin master

git branch -d feature/title-ko

---

< A와 B가 다른팀일 때>

`Fork` 버튼 클릭

git branch dltmddk1023

git add .

git commit -m "fix korean"

git push origin dltmddk1023



----

![image-20201016114931436](git%20branch%20featurenav.assets/image-20201016114931436.png)



---

![image-20201016115003124](git%20branch%20featurenav.assets/image-20201016115003124.png)

**python manage.py loaddata movies.json**

git branch feature/recommended

git switch feature recommended

git commit -m "migrate&load_data"

![image-20201016120228506](git%20branch%20featurenav.assets/image-20201016120228506.png)



