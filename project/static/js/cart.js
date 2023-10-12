var updateBtns=document.getElementsByClassName('update-cart')
for(var i =0;i<updateBtns.length;i++){
  updateBtns[i].addEventListener('click',function(){
    var productId=this.dataset.product
    var action=this.dataset.action
    console.log('productId',productId,'action:',action)
    console.log("user:", user)
    if(user==='AnonymousUser'){
      addCookieItem(productId, action)
    }
		else{
			updateUserOrder(productId, action)
    }

  })
}

function updateUserOrder(productId, action){//لاضافة المنتج الى الكارت
	console.log('User is authenticated, sending data...')

	var url = '/update_item/'//نحدد لوين نرسلها (api)

	fetch(url, {
		method:'POST',//حددنا نوعها
		headers:{
			'Content-Type':'application/json',
			'X-CSRFToken':csrftoken,  //script in products
		}, 
		body:JSON.stringify({'productId':productId , 'action':action})
	})
	.then((response) => {//لتحويل لبيانات json
		return response.json()
	})
	.then((data) => {//التحكم بالبيانات
    console.log('data:' , data)
		location.reload()
	});
}

function addCookieItem(productId, action){
	console.log('User is not authenticated')

	if (action == 'add'){
		if (cart[productId] == undefined){
		cart[productId] = {'quantity':1}

		}else{
			cart[productId]['quantity'] += 1
		}
	}

	if (action == 'remove'){
		cart[productId]['quantity'] -= 1

		if (cart[productId]['quantity'] <= 0){
			console.log('Item should be deleted')
			delete cart[productId];
		}
	}
	console.log('CART:', cart)
	document.cookie ='cart=' + JSON.stringify(cart) + ";domain=;path=/"
	location.reload()

}


let spann=document.getElementsByClassName('pred')
s=document.getElementsByClassName('price')
console.log(spann)
for (i = 0; i < spann.length; i++) {
if(spann[i].innerText =='None$'){
	spann[i].style.display = 'none';
     s[i].style.textDecoration ='none'
		 s[i].style.color ='black'

}
}
// for (i = 0; i < s.length; i++) {

// }
// //slide show
// slide=document.getElementById('slide')
// var i=0
// var img=["static/image/jkjj.png","static/image/iphone.png","static/image/lap.png"] //مصفوفة الصور الي بدي ينعرضو
// var slideshow=function(){slide.src=img[i] //من اتش تي ام ال سميت ال امج سليدشو 
// if(i<img.length-1) 
// {i++}else{i=0/*رجعلي ع اول صورة*/}
// setTimeout("slideshow()",7000)}//اسم التابع والمدة لتتغير
//   slideshow()
