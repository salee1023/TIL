// 1. 배경 색상 변경
const body = document.querySelector('body')
body.id = 'main'


// 2. 요소 가운데 정렬
const nav = document.querySelector('nav')
const header = document.querySelector('header')
const section = document.querySelector('section')

nav.classList.add('box-container')
header.classList.add('box-container')
section.classList.add('box-container')


// 3. border 설정
const formDivList = document.querySelectorAll('form > div')
formDivList.forEach(function (div) {
    console.log(div)
    div.classList.add('box-item')
})

// 4. 버튼
const button = document.querySelector('form > input')
button.value = '제출'
button.classList.add('button')


// 5. input & select 스타일 변경
const inputName = document.querySelector('#name')
inputName.style.marginTop = '7px'
inputName.style.padding = '12px'

const selectRegion = document.querySelector('#region')
selectRegion.style.display = 'block'

// 6. 이미지 변경
const mainImage = document.querySelector('nav > a > img')
mainImage.src = 'https://zzu.li/ssafy-image'
mainImage.width = '600'