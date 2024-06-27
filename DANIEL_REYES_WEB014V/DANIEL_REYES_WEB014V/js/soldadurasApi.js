//implementando api FETCH
function mostrarSoldaduras(){
    let url='http://localhost:3300/soldaduras';//importacion de api
    fetch(url)//fetch pregunta que hacer con la url
    .then(response => response.json())//conversion a json
    .then(data => soldadurasApi(data))//manda la informacion a soldadurasApi(data)
    .catch(error => console.log(error))//captura error y enviar a consola

  
    const soldadurasApi=(data)=>{
        console.log(data)
        let texto=""

        for (i=0; i <data.length; i++){
            texto += `<tr>
                <td>${data[i].id}</td>
                <td>${data[i].tipo}</td>
                <td>${data[i].material}</td>
                <td>${data[i].aplicacion}</td>
                </tr>`
        }//for
        document.getElementById('soldApi').innerHTML=texto;
    }
}


