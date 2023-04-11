function ready(){
    //document.getElementById("divPaso2").style.display = "none"
    //document.getElementById("divPaso3").style.display = "none"
}
function paso1(){
    var fservicio = document.getElementById("f_servicio").value  
    var caudal = document.getElementById("caudal").value
    var te = document.getElementById("te").value
    var ts = document.getElementById("ts").value
    const c1 = 1000
    const c2 = 0.0003069
    var tDT = Number(caudal*(te - ts)*fservicio*c1*c2)
    alert ("El tamaño del Distrito Termino en TR es: "+tDT)
    document.getElementById("divPaso2").style.display = "block"
    paso2(tDT)
}
function paso2(tDT){
    var c500 = document.getElementById("c500").value  
    var c750 = document.getElementById("c750").value
    var c1000 = document.getElementById("c1000").value
    var aa500 = document.getElementById("aa500").value  
    var a750 = document.getElementById("a750").value
    var a1000 = document.getElementById("a1000").value
    var totalc= (500*c500)+(750*c750)+(1000*c1000)
    var totala= (500*aa500)+(750*a750)+(1000*a1000)
    var totales = totala + totalc
    var tmax = tDT + (tDT*0.5)

    var rp=totalc*0.3190995427365	
    var g=(totalc*511.13199046407)/1000	
    var c=(totalc*0.0035174111853)*(1925000/0.88)	
    var o=c*0.03	
    	
    var capex=totalc*0.0035174111853	
    var ft=capex*1000000	
    var e=capex*1700000	
    var b=capex*2000000

    paso3(rp,g,c,o,capex,ft,e,b,totalc)
}
function paso3(rp,g,c,o,capex,ft,e,b,totalc){
    const tabla = document.getElementById('divPaso3')
    tabla.innerHTML=
        `<h1>Div Paso 3</h1>
        <h1>Centrífugo</h1>
        <table class="table">
            <thead>
                <tr>
                    <th scope="col">Energía</th>
                    <th scope="col">Emisiones CO2(TCo2 al mes)</th>
                    <th scope="col">Capex(Dolares por Megavatios)</th>
                    <th scope="col">Opex(Dolares al año)</th>
                </tr>
            </thead>
            <tbody id="fila1">
                <tr>
                    <th scope="row">Red Pública</th>
                    <td>${e}</td>
                    <td>${g}</td>
                    <td>${ft}</td>
                </tr>
            </tbody>
            <tbody id="fila2">
                <tr>
                    <th scope="row">Microturbina a gas</th>
                    <td>${rp}</td>
                    <td>${o}</td>
                    <td>${rp}</td>
                </tr>
            </tbody>
            <tbody id="fila3">
                <tr>
                    <th scope="row">Solar fotovoltaica</th>
                    <td>${b}</td>
                    <td>${b}</td>
                    <td>${e}</td>
                </tr>
            </tbody>
            <tbody id="fila4">
                <tr>
                    <th scope="row">Energía eólica</th>
                    <td>${ft}</td>
                    <td>${ft}</td>
                    <td>${c}</td>
                </tr>
            </tbody>
            <tbody id="fila5">
                <tr>
                    <th scope="row">Energía biomasa</th>
                    <td>${c}</td>
                    <td>${capex}</td>
                    <td>${g}</td>
                </tr>
            </tbody>
            <tbody id="fila6">
                <tr>
                    <th scope="row">Toneladas de refrigeración que suministran los chillers centrífugos seleccionados es: </th>
                    <td>${totalc}</td>
                    <td>${" "}</td>
                    <td>${" "}</td>
                </tr>
            </tbody>
        </table>`
}