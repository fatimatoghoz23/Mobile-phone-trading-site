
var data= {
    chatinit:{
        title: ["Hello <span class='emoji'> &#128075;</span>","I am Mr. Chatbot","How can I help you?"],
        options: ["products <span class='emoji'> &#128250;</span>","checkout","Shopping <span class='emoji'> &#128090;</span>","cart <span class='emoji'> &#127925;</span>"]
    },
    products: {
        title:["Please select category"],
        options:['mobiles','laptops','taplets'],
        url : {
            
        }
    },
    lstorage: {
        title:["Thanks ","These are some results based on your input"],
        options:['laptop ram4','laptop ram8'],
        url : { 
        }
    },
   
    checkout: {
        title:[""],
        options:["checkout"],
        url : {
            link:["http://127.0.0.1:8000/checkout/"]
        }
    },
    shopping: {
        title:["Thanks for your response","Welcome to shopping zone <span class='emoji'> &#128090;</span>","Please select one of the below options to proceed further"],
        options:['mobils','laptops'],
        url : {
            
        }
    },
    electronics: {
        title:["Thanks for your response","Here are some electronic items for you","Click on it to know more"],
        options:['Televisions','Cameras','Gaming Consoles','Headphones','Speakers'],
        url : {
            link:["#","#","#","#","#"]
        }
    },
    beauty: {
        title:["Thanks for your response","Here are some beauty products for you","Click on it to know more"],
        options:['Make-up & Nails','Skin Care','Fragrance','Hair care'],
        url : {
            link:["#","#","#","#"]
        }
    },
    mobiles: {
        title:["Thanks ","These are some results based on your input","helllo"],
        options:['prices','storage','marka','discounts'],
        url : { 
        }
    },
    marka: {
        title:["Thanks ","These are some results based on your input","helllo"],
        options:['samsung','iphone','redmi'],
        url : { 
        }
    },
    storage: {
        title:["Thanks ","These are some results based on your input","helllo"],
        options:['ram4','ram8','ram16','ram32'],
        url : { 
        }
    },
    prices: {
        title:["Thanks ","These are some results based on your input","helllo"],
        options:['less than 100','less than 500','more than 500'],
        url : { 
        }
    },
    men: {
        title:["Thanks for your response","These are some results based on your input","Click on it to know more"],
        options:['Clothing','Shirts','T-shirts','Innerwear','Jeans'],
        url : {
            link:["#","#","#","#","#"]
        }
    },
    women: {
        title:["Thanks for your response","These are some results based on your input","Click on it to know more"],
        options:['Clothing','Western Wear','Ethnic Wear','Top Brands'],
        url : {
            link:["#","#","#","#"]
        }
    },
    cart: {
        title:[""],
        options: ['click to cart'],
        url : {
            link:["http://127.0.0.1:8000/cart/"]
        }
    },
    hollywood: {
        title: ["Thanks for your response","Here are some genre based movies"],
        options: ["Comedy","Horror","Sci-Fi","Romance","Action"],
        url: {
            link:["#","#","#","#","#"]
        }
    },
    bollywood: {
        title: ["Thanks for your response","Here are some genre based movies"],
        options: ["Comedy","Horror","Sci-Fi","Romance","Action"],
        url: {
            link:["#","#","#","#","#"]
        }
    },
    web: {
        title: ["Thanks for your response","Here are some genre based web series"],
        options: ["Comedy","Horror","Sci-Fi","Romance","Action"],
        url: {
            link:["#","#","#","#","#"]
        }
    },
    others: {
        title: ["Here are some more options for you"],
        options: ["YouTube","Netflix","Amazon Prime","Hot Star"],
        url: {
            link:["#","#","#","#","#"]
        }
    },
    laptops: {
        title:["Please select category"],
        options:['lprices','lstorage','laptop discounts'],
        url : {
            
        }
    },
    
    lprices: {
        title:["Thanks ","These are some results based on your input"],
        options:['laptop less than 1000','laptop more than 1000 '],
        url : { 
        }
    },

}


document.getElementById("init").addEventListener("click",showChatBot);
var cbot= document.getElementById("chat-box");
var len1= data.chatinit.title.length;
var options=['ram4','ram8','ram16','ram32']
function showChatBot(){
    console.log(this.innerText);
    if(this.innerText=='START CHAT'){
        document.getElementById('test').style.display='block';
        document.getElementById('init').innerText='CLOSE CHAT';

        initChat();
        
    }
    else{

        location.reload();

    }
}

function initChat(){
    j=0;
    cbot.innerHTML='';
    for(var i=0;i<len1;i++){
        setTimeout(handleChat,(i*500));
    }
    setTimeout(function(){
        showOptions(data.chatinit.options)
    },((len1+1)*500))
}

var j=0;
function handleChat(){
    console.log(j);
    var elm= document.createElement("p");
    elm.innerHTML= data.chatinit.title[j];
    elm.setAttribute("class","msg");
    cbot.appendChild(elm);
    j++;
    handleScroll();
}

function showOptions(options){
    for(var i=0;i<options.length;i++){
        var opt= document.createElement("span");
        var inp= '<option onclick="chatbot(options)" data-options="options">'+options[i]+'</option>';
        opt.innerHTML=inp;
        opt.setAttribute("data-options","options");
        opt.setAttribute("class","opt");
        opt.addEventListener("click", handleOpt);
        cbot.appendChild(opt);

        handleScroll();

    }


}
function chatbot(options){
	console.log('User is authenticated, sending data...')

	var url = '/chatbot/'//نحدد لوين نرسلها (api)

	fetch(url, {
		method:'POST',//حددنا نوعها
		headers:{
			'Content-Type':'application/json',
			'X-CSRFToken':csrftoken,  //script in products
		}, 
		body:JSON.stringify({'options':options})
	})
	.then((response) => {//لتحويل لبيانات json
		return response.json()
	})
	.then((datas) => {//التحكم بالبيانات
    console.log('datas:' , datas)
   
	});
    
       
}
function handleOpt(){
    console.log(this);
    var str= this.innerText;
    var textArr= str.split(" ");
    var findText= textArr[0];
    
    document.querySelectorAll(".opt").forEach(el=>{
        el.remove();
    })
    // var elm= document.createElement("p");
    // elm.setAttribute("class","test");
    // var sp= '<span class="rep" >'+this.innerText+'</span>';

    // elm.innerHTML= sp;
    // cbot.appendChild(elm);
    
    var url = '/chatbot/'//نحدد لوين نرسلها (api)

	fetch(url, {
		method:'POST',//حددنا نوعها
		headers:{
			'Content-Type':'application/json',
			'X-CSRFToken':csrftoken,  //script in products
		}, 
		body:JSON.stringify({})
	})
	.then((response) => {//لتحويل لبيانات json
		return response.json()
	})
	.then((datas) => {//التحكم بالبيانات
    console.log('datas:' , datas)
    if (this.innerText === 'ram4' || this.innerText === 'ram8' || this.innerText === 'less than 100'||this.innerText==='laptop ram4'
    ||this.innerText==='laptop more than 1000'||this.innerText==='samsung'||this.innerText=='less than 500'
    ||this.innerText=='more than 500'||this.innerText=='laptop less than 1000'||this.innerText==='laptop ram8' 
    ||this.innerText=='discounts'||this.innerText== 'laptop discounts'){
        var elms= document.createElement("div");
        elms.setAttribute("id","testt");
        var sp= '<div id="testt" ></div>';
        elms.innerHTML= sp;
        cbot.appendChild(elms);
        var rr=JSON.parse(datas)
        if (this.innerText=='ram4'){
            var dictionary1 = Object.assign({}, ...rr.map((x) => ({[x.pk]:x.fields})));
        document.getElementById("testt").innerHTML =JSON.stringify(Object.values(dictionary1).filter(item => item.ram === 4).filter(item => item.category === 'photo'),['name','price'])
        .replaceAll(/[`%^&*()_|+\-=?;'"<>\{\}\[\]\\\/]/gi, ' ').replaceAll("name",'product')
        handleScroll()
        }
      else if (this.innerText=='ram8' ){
            var dictionary1 = Object.assign({}, ...rr.map((x) => ({[x.pk]:x.fields})));
            document.getElementById("testt").innerHTML =JSON.stringify(Object.values(dictionary1).filter(item => item.ram === 8 ).filter(item => item.category === 'photo')
            ,['name','price']).replaceAll(/[`%^&*()_|+\-=?;'"<>\{\}\[\]\\\/]/gi, ' ').replaceAll("name",'product')
            handleScroll()
         }
        else if (this.innerText=='less than 100' ){    
            var dictionary1 = Object.assign({}, ...rr.map((x) => ({[x.pk]:x.fields})));
            document.getElementById("testt").innerHTML =JSON.stringify(Object.values(dictionary1).filter(item => item.price <= 100 ).filter(item => item.category === 'photo')
            ,['name','price']).replaceAll(/[`%^&*()_|+\-=?;'"<>\{\}\[\]\\\/]/gi, ' ').replaceAll("name",'product')
            handleScroll()}
       else if (this.innerText=='less than 500' ){    
                var dictionary1 = Object.assign({}, ...rr.map((x) => ({[x.pk]:x.fields})));
                document.getElementById("testt").innerHTML =JSON.stringify(Object.values(dictionary1).filter(item => item.price <= 500 ).filter(item => item.category === 'photo')
                ,['name','price']).replaceAll(/[`%^&*()_|+\-=?;'"<>\{\}\[\]\\\/]/gi, ' ').replaceAll("name",'product')
                handleScroll()}   
       else if (this.innerText=='more than 500' ){    
                    var dictionary1 = Object.assign({}, ...rr.map((x) => ({[x.pk]:x.fields})));
                    document.getElementById("testt").innerHTML =JSON.stringify(Object.values(dictionary1).filter(item => item.price >= 500 ).filter(item => item.category === 'photo')
                    ,['name','price']).replaceAll(/[`%^&*()_|+\-=?;'"<>\{\}\[\]\\\/]/gi, ' ').replaceAll("name",'product')
                    handleScroll()}    
       else if (this.innerText=='laptop ram4' ){
          var dictionary1 = Object.assign({}, ...rr.map((x) => ({[x.pk]:x.fields})));
          document.getElementById("testt").innerHTML =JSON.stringify(Object.values(dictionary1).filter(item => item.ram === 4 ).filter(item => item.category === 'computer')
          ,['name','price']).replaceAll(/[`%^&*()_|+\-=?;'"<>\{\}\[\]\\\/]/gi, ' ').replaceAll("name",'product')
          handleScroll()
            }
       else if (this.innerText=='laptop ram8' ){
                var dictionary1 = Object.assign({}, ...rr.map((x) => ({[x.pk]:x.fields})));
                document.getElementById("testt").innerHTML =JSON.stringify(Object.values(dictionary1).filter(item => item.ram === 8 ).filter(item => item.category === 'computer')
                ,['name','price']).replaceAll(/[`%^&*()_|+\-=?;'"<>\{\}\[\]\\\/]/gi, ' ').replaceAll("name",'product')
                handleScroll()
                  }
            else if (this.innerText=='laptop less than 1000' ){
                var dictionary1 = Object.assign({}, ...rr.map((x) => ({[x.pk]:x.fields})));
                document.getElementById("testt").innerHTML =JSON.stringify(Object.values(dictionary1).filter(item => item.price <=1000 ).filter(item => item.category === 'computer')
                ,['name','price']).replaceAll(/[`%^&*()_|+\-=?;'"<>\{\}\[\]\\\/]/gi, ' ').replaceAll("name",'product')
                handleScroll()
                  }
                  else if (this.innerText=='laptop more than 1000' ){
                    var dictionary1 = Object.assign({}, ...rr.map((x) => ({[x.pk]:x.fields})));
                    document.getElementById("testt").innerHTML =JSON.stringify(Object.values(dictionary1).filter(item => item.price >=1000 ).filter(item => item.category === 'computer')
                    ,['name','price']).replaceAll(/[`%^&*()_|+\-=?;'"<>\{\}\[\]\\\/]/gi, ' ').replaceAll("name",'product')
                    handleScroll()
                      }
             else if (this.innerText=='discounts' ){  
                    var dictionary1 = Object.assign({}, ...rr.map((x) => ({[x.pk]:x.fields})));
                    document.getElementById("testt").innerHTML =JSON.stringify(Object.values(dictionary1).filter(item => item.price2 != null ).filter(item => item.category === 'photo')
                    ,['name']).replaceAll(/[`%^&:*()_|+\-=?;'"<>\{\}\[\]\\\/]/gi, ' ').replaceAll("name",'')
                   
                    
                    handleScroll()
                      }
             else if (this.innerText=='laptop discounts' ){  
                        var dictionary1 = Object.assign({}, ...rr.map((x) => ({[x.pk]:x.fields})));
                        document.getElementById("testt").innerHTML =JSON.stringify(Object.values(dictionary1).filter(item => item.price2 != null ).filter(item => item.category === 'computer')
                        ,['name']).replaceAll(/[`%^&:*()_|+\-=?;'"<>\{\}\[\]\\\/]/gi, ' ').replaceAll("name",'')
                       
          
    }   
    } 
});
    
       

    console.log(findText.toLowerCase());
    var tempObj= data[findText.toLowerCase()];
    handleResults(tempObj.title,tempObj.options,tempObj.url);

    }

function handleDelay(title){
    var elm= document.createElement("p");
        elm.innerHTML= title;
        elm.setAttribute("class","msg");

        if(title==''){
           elm.style.display='none';


        }
        cbot.appendChild(elm);
}


function handleResults(title,options,url){
    for(let i=0;i<title.length;i++){
        setTimeout(function(){
            handleDelay(title[i]);
        },i*500)
        
    }

    const isObjectEmpty= (url)=>{
        return JSON.stringify(url)=== "{}";
    }

    if(isObjectEmpty(url)==true){
        console.log("having more options");
        setTimeout(function(){
            showOptions(options);
        },title.length*500)

    }
    else{
        console.log("end result");
        setTimeout(function(){
            handleOptions(options,url)
        },title.length*500)

    }
}

// var action="options"

function handleOptions(options,url,name){
    
    for(var i=0;i<options.length;i++){

        var opt= document.createElement("span");
        var inp= '<a class="m-link" data-options="options" onclick="chatbot(options)" href="'+url.link[i]+'">'+options[i]+'</a>';
        
        opt.innerHTML=inp;

        opt.setAttribute("class","opt");
        cbot.appendChild(opt);
        
        // opt.addEventListener("click",chatbot)
    }



    var opt= document.createElement("span");
    var inp= '<a class="m-link" href="'+url.more+'">'+'See more</a>';

    const isObjectEmpty= (url)=>{
        return JSON.stringify(url)=== "{}";
        
    }

    console.log(isObjectEmpty(url));
    console.log(url);
    opt.innerHTML=inp;
    opt.setAttribute("class","opt link");

    cbot.appendChild(opt);

    handleScroll();

}

function handleScroll(){
    var elem= document.getElementById('chat-box');
    elem.scrollTop= elem.scrollHeight;

}

log=document.getElementById('log')
if(user==='AnonymousUser'){
   log.innerHTML = 'login'
}

