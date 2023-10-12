var updateBtnss=document.getElementById('update-chat')

  updateBtnss.addEventListener('click',function(){
    var action=this.dataset.action
    console.log('action:',action)
    chatbotlisten(action)
  })

function chatbotlisten(action){
	

	var url = '/chatbotlisten/'//نحدد لوين نرسلها (api)

	fetch(url, {
		method:'POST',//حددنا نوعها
		headers:{
			'Content-Type':'application/json',
			'X-CSRFToken':csrftoken,  //script in products
		}, 
		body:JSON.stringify({'action':action})
	})
	.then((response) => {//لتحويل لبيانات json
		return response.json()
	})
	.then((data) => {//التحكم بالبيانات
    console.log('data:' , data)
   
	});}

	updateBtnss.addEventListener('click',function(){
     var elms= document.createElement("div");
         elms.setAttribute("id","chat");
         var sp= '<div id="chat" >Talk about the brand you want <br><br><span >Wait a second </span> </div>';
         elms.innerHTML= sp;
         cbot.appendChild(elms);
         
		
			// document.getElementById('chat').style.display='block'
		
		 
  })