(window.webpackJsonp=window.webpackJsonp||[]).push([[7],{1802:function(e,t,r){"use strict";r.r(t);var a=r(0);const n=["#DA752E","#E5C209","#1441A0","#B86117","#4D430C","#1DB390","#B3331D","#088EB2","#417505","#E479A8","#F9F39E","#5782DC","#EBA97B","#A2AB60","#B291CF","#8DD2C2","#E6A19F","#3DC7E0","#98CE5B"];var i=r(1016),o=r(954),l=r(1465),s=r(9);const c=s.c.div`
  & {
    margin: 30px 0;
    padding: 30px;
    border: 1px solid #ccc;
    border-radius: 5px;
    position: relative;
  }
  .close {
    position: absolute;
    top: 15px;
    right: 15px;
    cursor: pointer;
    opacity: 0.5;
    font-size: 40px;
    line-height: 22px;
  }
  .close:hover {
    opacity: 1;
  }
  .grid-wrapper {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    grid-gap: 20px;
  }
  h3 {
    margin: 0 0 20px;
  }
  .box {
    cursor: pointer;
    width: 30px;
    height: 30px;
    border-radius: 5px;
    display: inline-block;
    margin: 0 20px 20px 0;
  }
  textarea {
    height: 184px;
    width: 100%;
    box-sizing: border-box;
    margin-bottom: 20px;
    padding: 5px;
    font-size: 14px;
    border-color: #ccc;
  }
`,p=s.c.button`
  & {
    margin: 0 20px 10px 0;
    -webkit-appearance: none;
    padding: 5px 15px;
    background: white;
    border: 1px solid #bbb;
    border-radius: 3px;
    cursor: pointer;
    text-transform: uppercase;
    font-size: 14px;
    color: #555;
  }
  &:hover {
    border-color: #888;
    color: #222;
  }
`;class m extends a.Component{constructor(e){super(e),this.openClose=(()=>{this.setState({open:!this.state.open,colors:this.props.colors.join(",\n")})}),this.handleChange=((e,t)=>{this.setState({selectedColor:e,selectedPosition:t})}),this.pickerChange=(e=>{const{colors:t}=this.props;t[this.state.selectedPosition]=e.hex,this.props.updateColor(t),this.setState({selectedColor:e.hex,colors:t.join(",\n")})}),this.colorsFromTextarea=(()=>{const e=this.state.colors.replace(/\"/g,"").replace(/ /g,"").replace(/\[/g,"").replace(/\]/g,"").replace(/\r?\n|\r/g,"").split(",");this.props.updateColor(e)}),this.updateTextArea=(e=>{this.setState({colors:e.target.value})}),this.state={open:!1,selectedColor:e.colors[0],selectedPosition:0,colors:e.colors.join(",\n")}}render(){if(!this.state.open)return a.createElement("div",{style:{display:"inline-block"}},a.createElement(p,{onClick:this.openClose},"Adjust Palette"));const{colors:e}=this.props;return a.createElement(c,null,a.createElement("div",{className:"close",role:"button",tabIndex:0,onClick:this.openClose,onKeyPress:e=>{13===e.keyCode&&this.openClose()}},"×"),a.createElement("div",{className:"grid-wrapper"},a.createElement("div",null,a.createElement("h3",null,"Select Color"),e.map((e,t)=>a.createElement("div",{key:`color-${t}`,className:"box",style:{background:e},role:"button",tabIndex:0,onKeyPress:r=>{13===r.keyCode&&this.handleChange(e,t)},onClick:()=>this.handleChange(e,t)}))),a.createElement("div",null,a.createElement("h3",null,"Adjust Color"),a.createElement("div",{style:{width:"225px"}},a.createElement(l.ChromePicker,{color:this.state.selectedColor,onChangeComplete:this.pickerChange}))),a.createElement("div",null,a.createElement("h3",null,"Paste New Colors"),a.createElement("textarea",{value:this.state.colors,onChange:this.updateTextArea}),a.createElement(p,{onClick:this.colorsFromTextarea},"Update Colors"))),a.createElement("div",{style:{marginTop:"30px"}},a.createElement("a",{href:`http://projects.susielu.com/viz-palette?colors=[${e.map(e=>`"${e}"`).join(",")}]&backgroundColor="white"&fontColor="black"`},"Evaluate This Palette with VIZ PALETTE")))}}m.defaultProps={metadata:{},height:500};var d=m;var h=({values:e,colorHash:t,valueHash:r,colors:n=[],setColor:i})=>a.createElement("div",{style:{marginTop:"20px"}},(e.length>18?[...e.filter((e,t)=>t<18),"Other"]:e).map((e,n)=>t[e]&&a.createElement("span",{style:{display:"inline-block",minWidth:"80px",margin:"5px"},key:`legend-item-${n}`},a.createElement("span",{style:{display:"inline-block",width:"20px",height:"20px",marginRight:"5px",borderRadius:"20px",marginBottom:"-5px",background:t[e]}}),a.createElement("span",{className:"html-legend-item"},e),r[e]&&r[e]>1&&`(${r[e]})`||"")),i&&a.createElement(d,{colors:n,updateColor:e=>{i(e)}})),b=r(1553),u=r.n(b);function g(e){let t="0.[00]a";return 0===e?"0":(e>1e14||e<1e-5?t="0.[000]e+0":e<1&&(t="0.[0000]a"),u()(e).format(t))}var y=r(1796);const x=Object(s.c)(y.a)`
  .button-text {
    margin: 0 10px 10px 0;
    -webkit-appearance: none;
    padding: 5px 15px;
    background: white;
    border: 1px solid #bbb;
    color: #555;
    border-radius: 3px;
    cursor: pointer;
  }
  .button-text.selected {
    border-color: #1d8bf1;
    color: #1d8bf1;
  }
  .button-text {
    margin-right: -1px;
    border-radius: 0;
  }
  .button-text:first-child {
    border-top-left-radius: 3px;
    border-bottom-left-radius: 3px;
  }
  .button-text:last-child {
    border-top-right-radius: 3px;
    border-bottom-right-radius: 3px;
  }
  .button-text.selected {
    background: white;
    color: #1d8bf1;
    z-index: 1;
    position: relative;
  }
`;var f=s.c.div`
  color: black;
  padding: 10px;
  z-index: 999999;
  min-width: 120px;
  background: white;
  border: 1px solid #888;
  border-radius: 5px;
  position: relative;

  transform: translate(
      ${e=>e.x<100?"0px":"calc(-50% + 7px)"},
      ${e=>e.y<100?"10px":"calc(-100% - 10px)"}
    )
    & p {
    font-size: 14px;
  }

  & h3 {
    margin: 0 0 10px;
  }

  &:before {
    ${e=>e.x<100?null:e.y<100?'\n      border-left: inherit;\n      border-top: inherit;\n      top: -8px;\n      left: calc(50% - 15px);\n      background: inherit;\n      content: "";\n      padding: 0px;\n      transform: rotate(45deg);\n      width: 15px;\n      height: 15px;\n      position: absolute;\n      z-index: 99;\n    ':'\n    border-right: inherit;\n    border-bottom: inherit;\n    bottom: -8px;\n    left: calc(50% - 15px);\n    background: inherit;\n    content: "";\n    padding: 0px;\n    transform: rotate(45deg);\n    width: 15px;\n    height: 15px;\n    position: absolute;\n    z-index: 99;\n  '}
  }
`;const k=[40,380];class E extends a.Component{constructor(e){super(e),this.brushing=((e,t)=>{const r=this.state.columnExtent;r[t]=e,this.setState({columnExtent:r})});const{options:t,data:r,schema:a}=this.props,{primaryKey:n}=t,i=function(e,t,r,a){const n={},i={};t.forEach(t=>{const r=[Math.min(...e.map(e=>e[t.name])),Math.max(...e.map(e=>e[t.name]))],a=Object(o.a)().domain(r).range([0,1]);n[t.name]=a;const l=Object(o.a)().domain(r).range([380,0]);i[t.name]=l});const l=[];return e.forEach(e=>{t.forEach(t=>{const i={metric:t.name,rawvalue:e[t.name],pctvalue:n[t.name](e[t.name])};r.forEach(t=>{"string"===t.type&&(i[t.name]=e[t.name])}),a.forEach(t=>{i[t]=e[t]}),l.push(i)})}),{dataPieces:l,scales:i}}(r,t.metrics,a.fields,n);this.state={filterMode:!0,data:i.dataPieces,dataScales:i.scales,columnExtent:t.metrics.reduce((e,t)=>(e[t.name]=[-1/0,1/0],e),{})}}shouldComponentUpdate(){return!0}render(){const{options:e,data:t}=this.props,{primaryKey:r,metrics:n,chart:o,colors:l}=e,{dim1:s}=o,{columnExtent:c,filterMode:p}=this.state,m=new Map;Object.keys(c).forEach(e=>{const t=c[e].sort((e,t)=>e-t);this.state.data.filter(r=>r.metric===e&&(r.pctvalue<t[0]||r.pctvalue>t[1])).forEach(e=>{m.set(r.map(t=>e[t]).join(","),!0)})});const d={},b=t.filter(e=>!m.get(r.map(t=>e[t]).join(","))),u=b.map(e=>r.map(t=>e[t]).join(" - ")),y={Other:"grey"};if(s&&"none"!==s){const{uniqueValues:e,valueHash:r}=b.reduce((e,t)=>{const r=t[s];return e.valueHash[r]=e.valueHash[r]&&e.valueHash[r]+1||1,e.uniqueValues=!e.uniqueValues.find(e=>e===r)&&[...e.uniqueValues,r]||e.uniqueValues,e},{uniqueValues:[],valueHash:{}});t.reduce((e,t)=>-1===e.indexOf(t[s])?[...e,t[s]]:e,[]).forEach((e,t)=>{y[e]=l[t%l.length]}),d.afterElements=e.length<=18?a.createElement(h,{values:e,colorHash:y,valueHash:r}):a.createElement("p",{style:{margin:"20px 0 5px"}},u.length," items")}return p||(d.annotations=n.map(e=>({label:"",metric:e.name,type:"enclose-rect",color:"green",disable:["connector"],coordinates:[{metric:e.name,pctvalue:c[e.name][0]},{metric:e.name,pctvalue:c[e.name][1]}]})).filter(e=>0!==e.coordinates[0].pctvalue||1!==e.coordinates[1].pctvalue)),a.createElement("div",null,a.createElement(x,null,a.createElement("button",{className:`button-text ${p?"selected":""}`,onClick:()=>this.setState({filterMode:!0})},"Filter"),a.createElement("button",{className:`button-text ${p?"":"selected"}`,onClick:()=>this.setState({filterMode:!1})},"Explore")),a.createElement(i.ResponsiveOrdinalFrame,Object.assign({data:this.state.data,oAccessor:"metric",rAccessor:"pctvalue",type:{type:"point",r:2},connectorType:e=>r.map(t=>e[t]).join(","),style:e=>({fill:m.get(r.map(t=>e[t]).join(","))?"lightgray":y[e[s]],opacity:m.get(r.map(t=>e[t]).join(","))?.15:.99}),connectorStyle:e=>({stroke:m.get(r.map(t=>e.source[t]).join(","))?"gray":y[e.source[s]],strokeWidth:m.get(r.map(t=>e.source[t]).join(","))?1:1.5,strokeOpacity:m.get(r.map(t=>e.source[t]).join(","))?.1:1}),responsiveWidth:!0,margin:{top:20,left:20,right:20,bottom:100},oPadding:40,pixelColumnWidth:80,interaction:p?{columnsBrush:!0,during:this.brushing,extent:Object.keys(this.state.columnExtent)}:null,pieceHoverAnnotation:!p,tooltipContent:e=>{const t=m.get(r.map(t=>e[t]).join(","))?"grey":y[e[s]];return a.createElement(f,{x:e.x,y:e.y},a.createElement("h3",null,r.map(t=>e[t]).join(", ")),e[s]&&a.createElement("h3",{style:{color:t}},s,": ",e[s]),a.createElement("p",null,e.metric,": ",e.rawvalue))},canvasPieces:!0,canvasConnectors:!0,oLabel:e=>a.createElement("g",null,a.createElement("text",{transform:"rotate(45)"},e),a.createElement("g",{transform:"translate(-20,-395)"},a.createElement(i.Axis,{scale:this.state.dataScales[e],size:k,orient:"left",ticks:5,tickFormat:e=>a.createElement("g",null,a.createElement("text",{fill:"white",stroke:"white",opacity:.75,strokeWidth:2,textAnchor:"end"},g(e)),a.createElement("text",{textAnchor:"end"},g(e)))})))},d)))}}E.defaultProps={metadata:{},height:500};var v=E,w=r(866);const T=Object(o.a)().domain([5,30]).range([8,16]).clamp(!0),C={force:e=>t=>({fill:e[t.source.id],stroke:e[t.source.id],strokeOpacity:.25}),sankey:e=>t=>({fill:e[t.source.id],stroke:e[t.source.id],strokeOpacity:.25}),matrix:e=>t=>({fill:e[t.source.id],stroke:"none"}),arc:e=>t=>({fill:"none",stroke:e[t.source.id],strokeWidth:t.weight||1,strokeOpacity:.75})},R={force:e=>t=>({fill:e[t.id],stroke:e[t.id],strokeOpacity:.5}),sankey:e=>t=>({fill:e[t.id],stroke:e[t.id],strokeOpacity:.5}),matrix:e=>e=>({fill:"none",stroke:"#666",strokeOpacity:1}),arc:e=>t=>({fill:e[t.id],stroke:e[t.id],strokeOpacity:.5})},M=[{type:"frame-hover"},{type:"highlight",style:{stroke:"red",strokeOpacity:.5,strokeWidth:5,fill:"none"}}],O={force:M,sankey:M,matrix:[{type:"frame-hover"},{type:"highlight",style:{fill:"red",fillOpacity:.5}}],arc:M},j={none:!1,static:!0,scaled:e=>!e.nodeSize||e.nodeSize<5?null:a.createElement("text",{textAnchor:"middle",y:T(e.nodeSize)/2,fontSize:`${T(e.nodeSize)}px`},e.id)};var S=r(896),z=r(852);const $=(e,t)=>t=e.parent?$(e.parent,[e.key,...t]):["root",...t],P=(e,t)=>{if(0===t.depth)return"white";if(1===t.depth)return e[t.key];let r=t;for(let e=t.depth;e>1;e--)r=r.parent;return Object(z.interpolateLab)("white",e[r.key])(Math.max(0,t.depth/6))};function F(e,t){return"function"==typeof t?t(e):e[t]}const A=(e,t,r,a)=>{const n={};let i=[];return a.forEach(r=>{const a=F(r,e);n[a]||(n[a]={array:[],value:0,label:a},i.push(n[a])),n[a].array.push(r),n[a].value+=F(r,t)}),i=i.sort((e,t)=>t.value===e.value?e.label<t.label?-1:(e.label,t.label,1):t.value-e.value),"none"!==r&&i.forEach(e=>{e.array=e.array.sort((e,t)=>F(t,r)-F(e,r))}),i.reduce((e,t)=>[...e,...t.array],[])},N={heatmap:i.heatmapping,hexbin:i.hexbinning},B=Object(o.b)().domain([.01,.2,.4,.6,.8]).range(["none","#FBEEEC","#f3c8c2","#e39787","#ce6751","#b3331d"]);const L=(e,t,r,n="scatterplot")=>{const i=r.height-150||500,{chart:l,primaryKey:s,colors:c,setColor:p,dimensions:m}=r,{dim1:d,dim2:b,dim3:u,metric1:y,metric2:x,metric3:k}=l,E=e.filter(e=>e[y]&&e[x]&&(!k||"none"===k||e[k]));let v=()=>5;const w={Other:"grey"},T={};let C;if(b&&"none"!==b){const e=[...E].sort((e,t)=>t[y]-e[y]).filter((e,t)=>t<3),t=[...E].sort((e,t)=>t[x]-e[x]).filter(t=>-1===e.indexOf(t)).filter((e,t)=>t<3);C=function(e,t,r){const a=[],n={};return[...e,...t].forEach(e=>{const t=n[e[r]];if(t){const a=t.coordinates&&[...t.coordinates,e]||[e,t];Object.keys(n[e[r]]).forEach(t=>{delete n[e[r]][t]}),n[e[r]].id=e[r],n[e[r]].label=e[r],n[e[r]].type="react-annotation",n[e[r]].coordinates=a}else n[e[r]]=Object.assign({type:"react-annotation",label:e[r],id:e[r],coordinates:[]},e),a.push(n[e[r]])}),a}(e,t,b)}if(k&&"none"!==k){const e=Math.min(...E.map(e=>e[k])),t=Math.max(...E.map(e=>e[k]));v=Object(o.a)().domain([e,t]).range([2,20])}const R=A(y,"none"!==k&&k||x,"none",e);if(("scatterplot"===n||"contour"===n)&&d&&"none"!==d){const e=R.reduce((e,t)=>!e.find(e=>e===t[d].toString())&&[...e,t[d].toString()]||e,[]);e.forEach((e,t)=>{w[e]=t>18?"grey":c[t%c.length]}),T.afterElements=a.createElement(h,{valueHash:{},values:e,colorHash:w,setColor:p,colors:c})}let M=[];if("heatmap"===n||"hexbin"===n||"contour"===n&&"none"===u){if(M=[{coordinates:E}],"contour"!==n){const e=N[n]({areaType:{type:n,bins:10},data:{coordinates:E.map(e=>Object.assign({},e,{x:e[y],y:e[x]}))},size:[i,i]});M=e;const t=[.2,.4,.6,.8,1].map(t=>Math.floor(e.binMax*t)).reduce((e,t)=>0===t||-1!==e.indexOf(t)?e:[...e,t],[]),r=[0,...t],o=[];r.forEach((e,t)=>{const a=r[t+1];a&&o.push(`${e+1} - ${a}`)});const l=["#FBEEEC","#f3c8c2","#e39787","#ce6751","#b3331d"],s={};o.forEach((e,t)=>{s[e]=l[t]}),B.domain([.01,...t]).range(["none",...l.filter((e,r)=>r<t.length)]),T.afterElements=a.createElement(h,{valueHash:{},values:o,colorHash:s,colors:c})}}else if("contour"===n){const e={};M=[],E.forEach(t=>{e[t[d]]||(e[t[d]]={label:t[d],color:w[t[d]],coordinates:[]},M.push(e[t[d]])),e[t[d]].coordinates.push(t)})}const O=("scatterplot"===n||"contour"===n)&&e.length>999;return Object.assign({xAccessor:"hexbin"===n||"heatmap"===n?"x":y,yAccessor:"hexbin"===n||"heatmap"===n?"y":x,axes:[{orient:"left",ticks:6,label:x,tickFormat:g,baseline:"scatterplot"===n,tickSize:"heatmap"===n?0:void 0},{orient:"bottom",ticks:6,label:y,tickFormat:g,footer:"heatmap"===n,baseline:"scatterplot"===n,tickSize:"heatmap"===n?0:void 0}],points:("scatterplot"===n||"contour"===n)&&e,canvasPoints:O,areas:"scatterplot"!==n&&M,areaType:{type:n,bins:10,thresholds:"none"===u?6:3},areaStyle:e=>({fill:"contour"===n?"none":B((e.binItems||e.data.binItems).length),stroke:"contour"!==n?void 0:"none"===u?"#BBB":e.parentArea.color,strokeWidth:"contour"===n?2:1}),pointStyle:e=>({r:O?2:"contour"===n?3:v(e[k]),fill:w[e[d]]||"black",fillOpacity:.75,stroke:O?"none":"contour"===n?"white":"black",strokeWidth:"contour"===n?.5:1,strokeOpacity:.9}),hoverAnnotation:!0,responsiveWidth:!1,size:[i+225,i+80],margin:{left:75,bottom:50,right:150,top:30},annotations:"scatterplot"===n&&C||void 0,annotationSettings:{layout:{type:"marginalia",orient:"right",marginOffset:30}},tooltipContent:("hexbin"===n||"heatmap"===n)&&(e=>0===e.binItems.length?null:a.createElement(f,{x:e.x,y:e.y},a.createElement("h3",{style:{fontSize:"14px",textTransform:"uppercase",margin:"5px",fontWeight:900}},"ID, ",y,", ",x),e.binItems.map((e,t)=>{const r=m.map(t=>e[t.name].toString&&e[t.name].toString()||e[t.name]).join(",");return a.createElement("p",{key:r+t,style:{fontSize:"12px",textTransform:"uppercase",margin:"5px"}},r,", ",e[y],", ",e[x])})))||(e=>a.createElement(f,{x:e.x,y:e.y},a.createElement("h3",null,s.map(t=>e[t]).join(", ")),m.map(t=>a.createElement("p",{key:`tooltip-dim-${t.name}`},t.name,":"," ",e[t.name].toString&&e[t.name].toString()||e[t.name])),a.createElement("p",null,y,": ",e[y]),a.createElement("p",null,x,": ",e[x]),k&&"none"!==k&&a.createElement("p",null,k,": ",e[k])))},T)},G=Object(o.a)().domain([8,25]).range([14,8]).clamp(!0),K={line:{Frame:i.ResponsiveXYFrame,controls:"switch between linetype",chartGenerator:(e,t,r)=>{let n;const{chart:i,selectedMetrics:l,lineType:s,metrics:c,primaryKey:p,colors:m}=r,{timeseriesSort:d}=i,h=t.fields.find(e=>e&&e.name===d),b="array-order"===d?"integer":h&&h.type?h.type:null,u=e=>"datetime"===b?e.toLocaleString().split(",")[0]:g(e),y="datetime"===b?Object(o.c)():Object(o.a)();return n=c.map((t,r)=>{const a="array-order"===d?e:e.sort((e,t)=>e[d]-t[d]);return{color:m[r%m.length],label:t.name,type:t.type,coordinates:a.map((e,a)=>({value:e[t.name],x:"array-order"===d?a:e[d],label:t.name,color:m[r%m.length],originalData:e}))}}).filter(e=>0===l.length||l.some(t=>t===e.label)),{lineType:{type:s,interpolator:w.curveMonotoneX},lines:n,xScaleType:y,renderKey:(e,t)=>e.coordinates?`line-${e.label}`:`linepoint=${e.label}-${t}`,lineStyle:e=>({fill:"line"===s?"none":e.color,stroke:e.color,fillOpacity:.75}),pointStyle:e=>({fill:e.color,fillOpacity:.75}),axes:[{orient:"left",tickFormat:g},{orient:"bottom",ticks:5,tickFormat:e=>{const t=u(e),r=t.length>4?"45":"0",n=t.length>4?"start":"middle";return a.createElement("text",{transform:`rotate(${r})`,textAnchor:n},t)}}],hoverAnnotation:!0,xAccessor:"x",yAccessor:"value",showLinePoints:"line"===s,margin:{top:20,right:200,bottom:"datetime"===b?80:40,left:50},legend:{title:"Legend",position:"right",width:200,legendGroups:[{label:"",styleFn:e=>({fill:e.color}),items:n}]},tooltipContent:e=>a.createElement(f,{x:e.x,y:e.y},a.createElement("p",null,e.parentLine&&e.parentLine.label),a.createElement("p",null,e.value&&e.value.toLocaleString()||e.value),a.createElement("p",null,d,": ",u(e.x)),p.map((t,r)=>a.createElement("p",{key:`key-${r}`},t,":"," ",e.originalData[t].toString&&e.originalData[t].toString()||e.originalData[t])))}}},scatter:{Frame:i.ResponsiveXYFrame,controls:"switch between modes",chartGenerator:L},hexbin:{Frame:i.ResponsiveXYFrame,controls:"switch between modes",chartGenerator:(e,t,r)=>L(e,t,r,r.areaType)},bar:{Frame:i.ResponsiveOrdinalFrame,controls:"switch between modes",chartGenerator:(e,t,r)=>{const{selectedDimensions:n,chart:i,colors:o,setColor:l}=r,{dim1:s,metric1:c,metric3:p}=i,m=0===n.length?s:e=>n.map(t=>e[t]).join(","),d=c,b={},u={Other:"grey"},y=A(m,"none"!==p&&p||d,s,e);p&&"none"!==p&&(b.dynamicColumnWidth=p);const x=y.reduce((e,t)=>e.find(e=>e===t[s].toString())?e:[...e,t[s].toString()],[]);s&&"none"!==s&&(x.forEach((e,t)=>{u[e]=t>18?"grey":o[t%o.length]}),b.afterElements=a.createElement(h,{valueHash:{},values:x,colorHash:u,setColor:l,colors:o}),n.length>0&&n.join(",")!==s&&(b.pieceHoverAnnotation=!0,b.tooltipContent=(e=>a.createElement(f,{x:e.x,y:e.y},s&&"none"!==s&&a.createElement("p",null,e[s]),a.createElement("p",null,"function"==typeof m?m(e):e[m]),a.createElement("p",null,d,": ",e[d]),p&&"none"!==p&&a.createElement("p",null,p,": ",e[p])))));const k=n.length>0&&!(1===n.length&&s===n[0])&&y.map(e=>e[s]).reduce((e,t)=>-1===e.indexOf(t)?[...e,t]:e,[]).length||0;return Object.assign({type:k>4?"clusterbar":"bar",data:y,oAccessor:m,rAccessor:d,style:e=>({fill:u[e[s]]||o[0],stroke:u[e[s]]||o[0]}),oPadding:x.length>30?1:5,oLabel:!(x.length>30)&&(e=>a.createElement("text",{transform:"rotate(90)"},e)),hoverAnnotation:!0,margin:{top:10,right:10,bottom:100,left:70},axis:{orient:"left",label:d,tickFormat:g},tooltipContent:e=>a.createElement(f,{x:e.column.xyData[0].xy.x,y:e.column.xyData[0].xy.y},a.createElement("p",null,"function"==typeof m?m(e.pieces[0]):e.pieces[0][m]),a.createElement("p",null,d,":"," ",e.pieces.map(e=>e[d]).reduce((e,t)=>e+t,0)),p&&"none"!==p&&a.createElement("p",null,p,":"," ",e.pieces.map(e=>e[p]).reduce((e,t)=>e+t,0))),baseMarkProps:{forceUpdate:!0}},b)}},summary:{Frame:i.ResponsiveOrdinalFrame,controls:"switch between modes",chartGenerator:(e,t,r)=>{const n={},i={},{chart:o,summaryType:l,primaryKey:s,colors:c,setColor:p}=r,{dim1:m,metric1:d}=o,b=m,u=d,y=e.reduce((e,t)=>!e.find(e=>e===t[m].toString())&&[...e,t[m].toString()]||e,[]);return m&&"none"!==m&&(y.forEach((e,t)=>{i[e]=c[t%c.length]}),n.afterElements=a.createElement(h,{valueHash:{},values:y,colorHash:i,setColor:p,colors:c})),Object.assign({summaryType:{type:l,bins:16,amplitude:20},type:"violin"===l&&"swarm",projection:"horizontal",data:e,oAccessor:b,rAccessor:u,summaryStyle:e=>({fill:i[e[m]]||c[0],fillOpacity:.8,stroke:i[e[m]]||c[0]}),style:e=>({fill:i[e[m]]||c[0],stroke:"white"}),oPadding:5,oLabel:!(y.length>30)&&(e=>a.createElement("text",{textAnchor:"end",fontSize:`${e&&G(e.length)||12}px`},e)),margin:{top:25,right:10,bottom:50,left:100},axis:{orient:"left",label:u,tickFormat:g},baseMarkProps:{forceUpdate:!0},pieceHoverAnnotation:"violin"===l,tooltipContent:e=>a.createElement(f,{x:e.x,y:e.y},a.createElement("h3",null,s.map(t=>e[t]).join(", ")),a.createElement("p",null,m,": ",e[m]),a.createElement("p",null,u,": ",e[u]))},n)}},network:{Frame:i.ResponsiveNetworkFrame,controls:"switch between modes",chartGenerator:(e,t,r)=>{const{networkType:n="force",chart:i,colors:o}=r,{dim1:l,dim2:s,metric1:c,networkLabel:p}=i;if(!l||"none"===l||!s||"none"===s)return{};const m={},d=[];e.forEach(e=>{m[`${e[l]}-${e[s]}`]||(m[`${e[l]}-${e[s]}`]={source:e[l],target:e[s],value:0,weight:0},d.push(m[`${e[l]}-${e[s]}`])),m[`${e[l]}-${e[s]}`].value+=e[c]||1,m[`${e[l]}-${e[s]}`].weight+=1});const h={};return e.forEach(e=>{h[e[l]]||(h[e[l]]=o[Object.keys(h).length%o.length]),h[e[s]]||(h[e[s]]=o[Object.keys(h).length%o.length])}),d.forEach(e=>{e.weight=Math.min(10,e.weight)}),{edges:d,edgeType:"force"===n&&"halfarrow",edgeStyle:C[n](h),nodeStyle:R[n](h),nodeSizeAccessor:e=>e.degree,networkType:{type:n,iterations:1e3},hoverAnnotation:O[n],tooltipContent:e=>a.createElement(f,{x:e.x,y:e.y},a.createElement("h3",null,e.id),a.createElement("p",null,"Links: ",e.degree),e.value&&a.createElement("p",null,"Value: ",e.value)),nodeLabels:"matrix"!==n&&j[p],margin:{left:100,right:100,top:10,bottom:10}}}},hierarchy:{Frame:i.ResponsiveNetworkFrame,controls:"switch between modes",chartGenerator:(e,t,r)=>{const{hierarchyType:n="dendrogram",chart:i,selectedDimensions:o,primaryKey:l,colors:s}=r,{metric1:c}=i,p="sunburst"===n?"partition":n;if(0===o.length)return{};const m=Object(S.nest)();o.forEach(e=>{m.key(t=>t[e])});const d={},h=[];return e.forEach(e=>{d[e[o[0]]]||(d[e[o[0]]]=s[Object.keys(d).length]),h.push(Object.assign({},e,{sanitizedR:e.r,r:void 0}))}),{edges:{values:m.entries(h)},edgeStyle:()=>({fill:"lightgray",stroke:"gray"}),nodeStyle:e=>({fill:P(d,e),stroke:1===e.depth?"white":"black",strokeOpacity:.1*e.depth+.2}),networkType:{type:p,projection:"sunburst"===n&&"radial",hierarchySum:e=>e[c],hierarchyChildren:e=>e.values,padding:"treemap"===p?3:0},edgeRenderKey:(e,t)=>t,baseMarkProps:{forceUpdate:!0},margin:{left:100,right:100,top:10,bottom:10},hoverAnnotation:[{type:"frame-hover"},{type:"highlight",style:{stroke:"red",strokeOpacity:.5,strokeWidth:5,fill:"none"}}],tooltipContent:e=>a.createElement(f,{x:e.x,y:e.y},((e,t,r)=>{const n=e.parent?$(e.parent,e.key&&[e.key]||[]).join("->"):"",i=[];return e.parent?e.key?(i.push(a.createElement("h2",{key:"hierarchy-title"},e.key)),i.push(a.createElement("p",{key:"path-string"},n)),i.push(a.createElement("p",{key:"hierarchy-value"},"Total Value: ",e.value)),i.push(a.createElement("p",{key:"hierarchy-children"},"Children: ",e.children.length))):(i.push(a.createElement("p",{key:"leaf-label"},n,"->",t.map(t=>e[t]).join(", "))),i.push(a.createElement("p",{key:"hierarchy-value"},r,": ",e[r]))):i.push(a.createElement("h2",{key:"hierarchy-title"},"Root")),i})(e,l,c))}}},parallel:{Frame:v,controls:"switch between modes",chartGenerator:(e,t,r)=>({data:e,schema:t,options:r})}};var W=r(1783),Z=r(1554),D=r.n(Z),I=r(369),Y=r(824),X=r(1797),H=r(119),U=s.a`
  .ReactTable {
    position: relative;
    display: -webkit-box;
    display: -ms-flexbox;
    display: flex;
    -webkit-box-orient: vertical;
    -webkit-box-direction: normal;
    -ms-flex-direction: column;
    flex-direction: column;
    border: 1px solid rgba(0, 0, 0, 0.1);
  }
  .ReactTable * {
    box-sizing: border-box;
  }
  .ReactTable .rt-table {
    -webkit-box-flex: 1;
    -ms-flex: auto 1;
    flex: auto 1;
    display: -webkit-box;
    display: -ms-flexbox;
    display: flex;
    -webkit-box-orient: vertical;
    -webkit-box-direction: normal;
    -ms-flex-direction: column;
    flex-direction: column;
    -webkit-box-align: stretch;
    -ms-flex-align: stretch;
    align-items: stretch;
    width: 100%;
    border-collapse: collapse;
    overflow: auto;
  }
  .ReactTable .rt-thead {
    -webkit-box-flex: 1;
    -ms-flex: 1 0 auto;
    flex: 1 0 auto;
    display: -webkit-box;
    display: -ms-flexbox;
    display: flex;
    -webkit-box-orient: vertical;
    -webkit-box-direction: normal;
    -ms-flex-direction: column;
    flex-direction: column;
    -webkit-user-select: none;
    -moz-user-select: none;
    -ms-user-select: none;
    user-select: none;
  }
  .ReactTable .rt-thead.-headerGroups {
    background: rgba(0, 0, 0, 0.03);
    border-bottom: 1px solid rgba(0, 0, 0, 0.05);
  }
  .ReactTable .rt-thead.-filters {
    border-bottom: 1px solid rgba(0, 0, 0, 0.05);
  }
  .ReactTable .rt-thead.-filters input,
  .ReactTable .rt-thead.-filters select {
    border: 1px solid rgba(0, 0, 0, 0.1);
    background: #fff;
    padding: 5px 7px;
    font-size: inherit;
    border-radius: 3px;
    font-weight: normal;
    outline: none;
  }
  .ReactTable .rt-thead.-filters .rt-th {
    border-right: 1px solid rgba(0, 0, 0, 0.02);
  }
  .ReactTable .rt-thead.-header {
    box-shadow: 0 2px 15px 0 rgba(0, 0, 0, 0.15);
  }
  .ReactTable .rt-thead .rt-tr {
    text-align: center;
  }
  .ReactTable .rt-thead .rt-th,
  .ReactTable .rt-thead .rt-td {
    padding: 5px 5px;
    line-height: normal;
    position: relative;
    border-right: 1px solid rgba(0, 0, 0, 0.05);
    transition: box-shadow 0.3s cubic-bezier(0.175, 0.885, 0.32, 1.275);
    box-shadow: inset 0 0 0 0 transparent;
  }
  .ReactTable .rt-thead .rt-th.-sort-asc,
  .ReactTable .rt-thead .rt-td.-sort-asc {
    box-shadow: inset 0 3px 0 0 rgba(0, 0, 0, 0.6);
  }
  .ReactTable .rt-thead .rt-th.-sort-desc,
  .ReactTable .rt-thead .rt-td.-sort-desc {
    box-shadow: inset 0 -3px 0 0 rgba(0, 0, 0, 0.6);
  }
  .ReactTable .rt-thead .rt-th.-cursor-pointer,
  .ReactTable .rt-thead .rt-td.-cursor-pointer {
    cursor: pointer;
  }
  .ReactTable .rt-thead .rt-th:last-child,
  .ReactTable .rt-thead .rt-td:last-child {
    border-right: 0;
  }
  .ReactTable .rt-thead .rt-resizable-header {
    overflow: visible;
  }
  .ReactTable .rt-thead .rt-resizable-header:last-child {
    overflow: hidden;
  }
  .ReactTable .rt-thead .rt-resizable-header-content {
    overflow: hidden;
    text-overflow: ellipsis;
  }
  .ReactTable .rt-thead .rt-header-pivot {
    border-right-color: #f7f7f7;
  }
  .ReactTable .rt-thead .rt-header-pivot:after,
  .ReactTable .rt-thead .rt-header-pivot:before {
    left: 100%;
    top: 50%;
    border: solid transparent;
    content: " ";
    height: 0;
    width: 0;
    position: absolute;
    pointer-events: none;
  }
  .ReactTable .rt-thead .rt-header-pivot:after {
    border-color: rgba(255, 255, 255, 0);
    border-left-color: #fff;
    border-width: 8px;
    margin-top: -8px;
  }
  .ReactTable .rt-thead .rt-header-pivot:before {
    border-color: rgba(102, 102, 102, 0);
    border-left-color: #f7f7f7;
    border-width: 10px;
    margin-top: -10px;
  }
  .ReactTable .rt-tbody {
    -webkit-box-flex: 99999;
    -ms-flex: 99999 1 auto;
    flex: 99999 1 auto;
    display: -webkit-box;
    display: -ms-flexbox;
    display: flex;
    -webkit-box-orient: vertical;
    -webkit-box-direction: normal;
    -ms-flex-direction: column;
    flex-direction: column;
    overflow: auto;
  }
  .ReactTable .rt-tbody .rt-tr-group {
    border-bottom: solid 1px rgba(0, 0, 0, 0.05);
  }
  .ReactTable .rt-tbody .rt-tr-group:last-child {
    border-bottom: 0;
  }
  .ReactTable .rt-tbody .rt-td {
    border-right: 1px solid rgba(0, 0, 0, 0.02);
  }
  .ReactTable .rt-tbody .rt-td:last-child {
    border-right: 0;
  }
  .ReactTable .rt-tbody .rt-expandable {
    cursor: pointer;
    text-overflow: clip;
  }
  .ReactTable .rt-tr-group {
    -webkit-box-flex: 1;
    -ms-flex: 1 0 auto;
    flex: 1 0 auto;
    display: -webkit-box;
    display: -ms-flexbox;
    display: flex;
    -webkit-box-orient: vertical;
    -webkit-box-direction: normal;
    -ms-flex-direction: column;
    flex-direction: column;
    -webkit-box-align: stretch;
    -ms-flex-align: stretch;
    align-items: stretch;
  }
  .ReactTable .rt-tr {
    -webkit-box-flex: 1;
    -ms-flex: 1 0 auto;
    flex: 1 0 auto;
    display: -webkit-inline-box;
    display: -ms-inline-flexbox;
    display: inline-flex;
  }
  .ReactTable .rt-th,
  .ReactTable .rt-td {
    -webkit-box-flex: 1;
    -ms-flex: 1 0 0px;
    flex: 1 0 0;
    white-space: nowrap;
    text-overflow: ellipsis;
    padding: 7px 5px;
    overflow: hidden;
    transition: 0.3s ease;
    transition-property: width, min-width, padding, opacity;
  }
  .ReactTable .rt-th.-hidden,
  .ReactTable .rt-td.-hidden {
    width: 0 !important;
    min-width: 0 !important;
    padding: 0 !important;
    border: 0 !important;
    opacity: 0 !important;
  }
  .ReactTable .rt-expander {
    display: inline-block;
    position: relative;
    margin: 0;
    color: transparent;
    margin: 0 10px;
  }
  .ReactTable .rt-expander:after {
    content: "";
    position: absolute;
    width: 0;
    height: 0;
    top: 50%;
    left: 50%;
    -webkit-transform: translate(-50%, -50%) rotate(-90deg);
    transform: translate(-50%, -50%) rotate(-90deg);
    border-left: 5.04px solid transparent;
    border-right: 5.04px solid transparent;
    border-top: 7px solid rgba(0, 0, 0, 0.8);
    transition: all 0.3s cubic-bezier(0.175, 0.885, 0.32, 1.275);
    cursor: pointer;
  }
  .ReactTable .rt-expander.-open:after {
    -webkit-transform: translate(-50%, -50%) rotate(0);
    transform: translate(-50%, -50%) rotate(0);
  }
  .ReactTable .rt-resizer {
    display: inline-block;
    position: absolute;
    width: 36px;
    top: 0;
    bottom: 0;
    right: -18px;
    cursor: col-resize;
    z-index: 10;
  }
  .ReactTable .rt-tfoot {
    -webkit-box-flex: 1;
    -ms-flex: 1 0 auto;
    flex: 1 0 auto;
    display: -webkit-box;
    display: -ms-flexbox;
    display: flex;
    -webkit-box-orient: vertical;
    -webkit-box-direction: normal;
    -ms-flex-direction: column;
    flex-direction: column;
    box-shadow: 0 0 15px 0 rgba(0, 0, 0, 0.15);
  }
  .ReactTable .rt-tfoot .rt-td {
    border-right: 1px solid rgba(0, 0, 0, 0.05);
  }
  .ReactTable .rt-tfoot .rt-td:last-child {
    border-right: 0;
  }
  .ReactTable .rt-thead.-header .rt-th {
    background: var(--cm-background);
  }
  .ReactTable.-striped .rt-tr.-odd > div {
    background: var(--theme-app-bg);
  }
  .ReactTable.-striped .rt-tr.-even > div {
    background: var(--cm-background);
  }
  .ReactTable.-highlight .rt-tbody .rt-tr:not(.-padRow):hover {
    background: rgba(0, 0, 0, 0.05);
  }
  .ReactTable .-pagination {
    z-index: 1;
    display: -webkit-box;
    display: -ms-flexbox;
    display: flex;
    -webkit-box-pack: justify;
    -ms-flex-pack: justify;
    justify-content: space-between;
    -webkit-box-align: stretch;
    -ms-flex-align: stretch;
    align-items: stretch;
    -ms-flex-wrap: wrap;
    flex-wrap: wrap;
    padding: 3px;
    box-shadow: 0 0 15px 0 rgba(0, 0, 0, 0.1);
    border-top: 2px solid rgba(0, 0, 0, 0.1);
  }
  .ReactTable .-pagination input,
  .ReactTable .-pagination select {
    border: 1px solid rgba(0, 0, 0, 0.1);
    background: #fff;
    padding: 5px 7px;
    font-size: inherit;
    border-radius: 3px;
    font-weight: normal;
    outline: none;
  }
  .ReactTable .-pagination .-btn {
    -webkit-appearance: none;
    -moz-appearance: none;
    appearance: none;
    display: block;
    width: 100%;
    height: 100%;
    border: 0;
    border-radius: 3px;
    padding: 6px;
    font-size: 1em;
    color: var(--theme-app-fg);
    background: var(--cm-background);
    transition: all 0.1s ease;
    cursor: pointer;
    outline: none;
  }
  .ReactTable .-pagination .-btn[disabled] {
    opacity: 0.5;
    cursor: default;
  }
  .ReactTable .-pagination .-btn:not([disabled]):hover {
    background: rgba(0, 0, 0, 0.3);
    color: #fff;
  }
  .ReactTable .-pagination .-previous,
  .ReactTable .-pagination .-next {
    -webkit-box-flex: 1;
    -ms-flex: 1;
    flex: 1;
    text-align: center;
  }
  .ReactTable .-pagination .-center {
    -webkit-box-flex: 1.5;
    -ms-flex: 1.5;
    flex: 1.5;
    text-align: center;
    margin-bottom: 0;
    display: -webkit-box;
    display: -ms-flexbox;
    display: flex;
    -webkit-box-orient: horizontal;
    -webkit-box-direction: normal;
    -ms-flex-direction: row;
    flex-direction: row;
    -ms-flex-wrap: wrap;
    flex-wrap: wrap;
    -webkit-box-align: center;
    -ms-flex-align: center;
    align-items: center;
    -ms-flex-pack: distribute;
    justify-content: space-around;
  }
  .ReactTable .-pagination .-pageInfo {
    display: inline-block;
    margin: 3px 10px;
    white-space: nowrap;
  }
  .ReactTable .-pagination .-pageJump {
    display: inline-block;
  }
  .ReactTable .-pagination .-pageJump input {
    width: 70px;
    text-align: center;
  }
  .ReactTable .-pagination .-pageSizeOptions {
    margin: 3px 10px;
  }
  .ReactTable .rt-noData {
    display: block;
    position: absolute;
    left: 50%;
    top: 50%;
    -webkit-transform: translate(-50%, -50%);
    transform: translate(-50%, -50%);
    background: rgba(255, 255, 255, 0.8);
    transition: all 0.3s ease;
    z-index: 1;
    pointer-events: none;
    padding: 20px;
    color: rgba(0, 0, 0, 0.5);
  }
  .ReactTable .-loading {
    display: block;
    position: absolute;
    left: 0;
    right: 0;
    top: 0;
    bottom: 0;
    background: rgba(255, 255, 255, 0.8);
    transition: all 0.3s ease;
    z-index: -1;
    opacity: 0;
    pointer-events: none;
  }
  .ReactTable .-loading > div {
    position: absolute;
    display: block;
    text-align: center;
    width: 100%;
    top: 50%;
    left: 0;
    font-size: 15px;
    color: rgba(0, 0, 0, 0.6);
    -webkit-transform: translateY(-52%);
    transform: translateY(-52%);
    transition: all 0.3s cubic-bezier(0.25, 0.46, 0.45, 0.94);
  }
  .ReactTable .-loading.-active {
    opacity: 1;
    z-index: 2;
    pointer-events: all;
  }
  .ReactTable .-loading.-active > div {
    -webkit-transform: translateY(50%);
    transform: translateY(50%);
  }
  .ReactTable .rt-resizing .rt-th,
  .ReactTable .rt-resizing .rt-td {
    transition: none !important;
    cursor: col-resize;
    -webkit-user-select: none;
    -moz-user-select: none;
    -ms-user-select: none;
    user-select: none;
  }
`;const q=D()(W.a),J=e=>{return{"=":">",">":"<","<":"="}[e]},Q=e=>{const{filterState:t,filterName:r,updateFunction:n,onChange:i}=e,o=t[r]||"=",l=a.createElement(I.a,{content:`Switch to ${J(o)}`},a.createElement(Y.a,{minimal:!0,onClick:()=>{n({[r]:J(o)})}},o));return a.createElement(X.a,{large:!0,placeholder:"number",rightElement:l,small:!1,type:"text",onChange:e=>{i(e.currentTarget.value)}})},_=(e,t,r)=>({onChange:n})=>a.createElement(Q,{onChange:n,filterState:e,filterName:t,updateFunction:r}),V=(e="=")=>(t,r)=>"="===e?r[t.id]==t.value:"<"===e?r[t.id]<t.value:">"===e?r[t.id]>t.value:r[t.id],ee={integer:_,number:_,string:()=>({onChange:e})=>a.createElement(X.a,{large:!0,placeholder:"string",type:"text",onChange:t=>{e(t.currentTarget.value)}})},te={integer:V,number:V,string:()=>(e,t)=>-1!==t[e.id].toLowerCase().indexOf(e.value.toLowerCase())};class re extends a.Component{constructor(e){super(e),this.state={filters:{},showFilters:!1}}render(){const{data:{data:e,schema:t},height:r}=this.props,{filters:n,showFilters:i}=this.state,o=t.fields.map(e=>"string"===e.type||"number"===e.type||"integer"===e.type?{Header:e.name,accessor:e.name,fixed:-1!==t.primaryKey.indexOf(e.name)&&"left",filterMethod:(t,r)=>{"string"!==e.type&&"number"!==e.type&&"integer"!==e.type||te[e.type](n[e.name])(t,r)},Filter:ee[e.type](n,e.name,e=>{this.setState({filters:Object.assign({},n,e)})})}:{Header:e.name,accessor:e.name,fixed:-1!==t.primaryKey.indexOf(e.name)&&"left"});return a.createElement("div",{style:{width:"calc(100vw - 150px)"}},a.createElement(Y.a,{icon:"filter",onClick:()=>this.setState({showFilters:!i})},i?"Hide":"Show"," Filters"),a.createElement(q,{data:e,columns:o,style:{height:`${r}px`},className:"-striped -highlight",filterable:i}),a.createElement(U,null),a.createElement(H.a,null))}}re.defaultProps={metadata:{},height:500};var ae=re,ne=r(1803),ie=r(1559),oe=r(814);const le="Line and stacked area charts for time series data where each row is a point and columns are data to be plotted.",se="Bar charts to compare individual and aggregate amounts.",ce="Scatterplot for comparing correlation between x and y values.",pe="A table of data.",me="Force-directed, adjacency matrix, arc diagram and sankey network visualization suitable for data that is an edge list where one dimension represents source and another dimension represents target.",de="Distribution plots such as boxplots and violin plots to compare.",he="Shows aggregate distribution of larger datasets across x and y metrics using hexbin, heatmap or contour plots.",be="Parallel coordinates for comparing and filtering across different values in the dataset.",ue="Nest data by categorical values using treemap, dendrogram, sunburst or partition.",ge={metric1:{default:"Plot this metric",scatter:"Plot this metric along the X axis",hexbin:"Plot this metric along the X axis"},metric2:{default:"Plot this metric along the Y axis"},metric3:{default:"Size the width of bars (Marimekko style) based on this metric",scatter:"Size the radius of points based on this metric"},dim1:{default:"Color items by this dimension",summary:"Group items into this category",network:"Use this dimension to determine the source node"},dim2:{default:"Label prominent datapoints using this dimension",network:"Use this dimension to determine the target node"},dim3:{default:"Split contours into separate groups based on this dimension"},networkType:"Represent network as a force-directed network (good for social networks) or as a sankey diagram (good for flow networks)",hierarchyType:"Represent your hierarchy as a tree (good for taxonomies) or a treemap (good for volumes) or partition (also good for volume where category volume is important)",timeseriesSort:"Sort line chart time series by its array position or by a specific metric or time",lineType:"Represent your data using a line chart, stacked area chart or ranked area chart",areaType:"Represent as a heatmap, hexbin or contour plot",lineDimensions:"Only plot the selected dimensions (or all if none are selected)"},ye=a.createElement(ie.a,{disabled:!0,text:"No results."}),xe=a.createElement("marker",{id:"arrow",refX:"3",refY:"3",markerWidth:"6",markerHeight:"6",orient:"auto-start-reverse"},a.createElement("path",{fill:"#5c7080",d:"M 0 0 L 6 3 L 0 6 z"})),fe={width:"16px",height:"16px",className:"bp3-icon"},ke=a.createElement("svg",Object.assign({},fe),a.createElement("defs",null,xe),a.createElement("polyline",{points:"3,3 3,13 12,13",fill:"none",stroke:"#5c7080",markerEnd:"url(#arrow)"})),Ee={Y:a.createElement("svg",Object.assign({},fe),a.createElement("defs",null,xe),a.createElement("polyline",{points:"3,3 3,13 12,13",fill:"none",stroke:"#5c7080",markerStart:"url(#arrow)"})),X:ke,Size:a.createElement("svg",Object.assign({},fe),a.createElement("circle",{cx:3,cy:13,r:2,fill:"none",stroke:"#5c7080"}),a.createElement("circle",{cx:6,cy:9,r:3,fill:"none",stroke:"#5c7080"}),a.createElement("circle",{cx:9,cy:5,r:4,fill:"none",stroke:"#5c7080"})),Color:a.createElement("svg",Object.assign({},fe),a.createElement("circle",{cx:3,cy:11,r:3,fill:"rgb(179, 51, 29)"}),a.createElement("circle",{cx:13,cy:11,r:3,fill:"rgb(87, 130, 220)"}),a.createElement("circle",{cx:8,cy:5,r:3,fill:"rgb(229, 194, 9)"}))},ve=(e,{handleClick:t,modifiers:r})=>{if(!r.matchesPredicate)return null;const n=`${e.label}`;return a.createElement(ie.a,{active:r.active,disabled:r.disabled,key:n,onClick:t,text:n})},we=(e,t)=>`${t.label.toLowerCase()}`.indexOf(e.toLowerCase())>=0,Te=e=>"X"===e||"Y"===e||"Size"===e||"Color"==e?Ee[e]:(console.warn("Icon title not supported"),e),Ce=s.b`
  h2 {
    text-transform: capitalize;
    margin-bottom: 10px;
  }
  select {
    height: 30px;
  }

  .selected {
    background-color: #d8e1e8 !important;
    background-image: none !important;
  }
`,Re=s.c.div`
  margin-right: 30px;
  ${Ce}
`,Me=s.c.div`
  display: flex;
  justify-content: left;
  margin-bottom: 30px;
  ${Ce}
`,Oe=(e,t,r,n,i,o="Help me help you help yourself")=>{const l=n?e:["none",...e];let s;return s=l.length>1?a.createElement(ne.a,{items:l.map(e=>({value:e,label:e})),query:i,noResults:ye,onItemSelect:(e,r)=>{t(e.value)},itemRenderer:ve,itemPredicate:we},a.createElement(Y.a,{icon:Te(r),text:i,rightIcon:"double-caret-vertical"})):a.createElement("p",{style:{margin:0}},l[0]),a.createElement(Re,{title:o},a.createElement("div",null,a.createElement(oe.a,null,r)),s)},je=[{type:"line",label:"Line Chart"},{type:"stackedarea",label:"Stacked Area Chart"},{type:"stackedpercent",label:"Stacked Area Chart (Percent)"},{type:"bumparea",label:"Ranked Area Chart"}],Se=[{type:"hexbin",label:"Hexbin"},{type:"heatmap",label:"Heatmap"},{type:"contour",label:"Contour Plot"}];var ze=({view:e,chart:t,metrics:r,dimensions:n,updateChart:i,selectedDimensions:o,selectedMetrics:l,hierarchyType:s,summaryType:c,networkType:p,setLineType:m,updateMetrics:d,updateDimensions:h,lineType:b,areaType:u,setAreaType:g,data:y})=>{const f=r.map(e=>e.name),k=n.map(e=>e.name),E=e=>r=>i({chart:Object.assign({},t,{[e]:r})}),v=(e,t)=>{if(Object.keys(ge).find(e=>e===t)){let r=t;const a=null!=ge[r]?ge[r]:null;return null==a?"":"string"==typeof a?a:null!=a[e]?a[e]:a.default}return""};return a.createElement(a.Fragment,null,a.createElement(Me,null,("summary"===e||"scatter"===e||"hexbin"===e||"bar"===e||"network"===e||"hierarchy"===e)&&Oe(f,E("metric1"),"scatter"===e||"hexbin"===e?"X":"Metric",!0,t.metric1,v(e,"metric1")),("scatter"===e||"hexbin"===e)&&Oe(f,E("metric2"),"Y",!0,t.metric2,v(e,"metric2")),("scatter"===e&&y.length<1e3||"bar"===e)&&Oe(f,E("metric3"),"bar"===e?"Width":"Size",!1,t.metric3,v(e,"metric3")),("summary"===e||"scatter"===e||"hexbin"===e&&"contour"===u||"bar"===e||"parallel"===e)&&Oe(k,E("dim1"),"summary"===e?"Category":"Color",!0,t.dim1,v(e,"dim1")),"scatter"===e&&Oe(k,E("dim2"),"Labels",!1,t.dim2,v(e,"dim2")),"hexbin"===e&&"contour"===u&&Oe(["by color"],E("dim3"),"Multiclass",!1,t.dim3,v(e,"dim3")),"network"===e&&Oe(k,E("dim1"),"SOURCE",!0,t.dim1,v(e,"dim1")),"network"===e&&Oe(k,E("dim2"),"TARGET",!0,t.dim2,v(e,"dim2")),"network"===e&&Oe(["matrix","arc","force","sankey"],e=>i({networkType:e}),"Type",!0,p,ge.networkType),"network"===e&&Oe(["static","scaled"],E("networkLabel"),"Show Labels",!1,t.networkLabel,ge.networkLabel),"hierarchy"===e&&Oe(["dendrogram","treemap","partition","sunburst"],e=>i({hierarchyType:e}),"Type",!0,s,ge.hierarchyType),"summary"===e&&Oe(["violin","boxplot","joy","heatmap","histogram"],e=>i({summaryType:e}),"Type",!0,c,ge.summaryType),"line"===e&&Oe(["array-order",...f],E("timeseriesSort"),"Sort by",!0,t.timeseriesSort,ge.timeseriesSort),"line"===e&&a.createElement("div",{title:ge.lineType,style:{display:"inline-block"}},a.createElement("div",null,a.createElement(oe.a,null,"Chart Type")),a.createElement(x,{vertical:!0},je.map(e=>a.createElement(Y.a,{key:e.type,className:`button-text ${b===e.type&&"selected"}`,active:b===e.type,onClick:()=>m(e.type)},e.label)))),"hexbin"===e&&a.createElement("div",{className:"control-wrapper",title:ge.areaType},a.createElement("div",null,a.createElement(oe.a,null,"Chart Type")),a.createElement(x,{vertical:!0},Se.map(e=>{const t=e.type;return"contour"===t||"hexbin"===t||"heatmap"===t?a.createElement(Y.a,{className:`button-text ${u===t&&"selected"}`,key:t,onClick:()=>g(t),active:u===t},e.label):a.createElement("div",null)}))),"hierarchy"===e&&a.createElement("div",{className:"control-wrapper",title:ge.nestingDimensions},a.createElement("div",null,a.createElement(oe.a,null,"Nesting")),0===o.length?"Select categories to nest":`root, ${o.join(", ")}`),("bar"===e||"hierarchy"===e)&&a.createElement("div",{className:"control-wrapper",title:ge.barDimensions},a.createElement("div",null,a.createElement(oe.a,null,"Categories")),a.createElement(x,{vertical:!0},n.map(e=>a.createElement(Y.a,{key:`dimensions-select-${e.name}`,className:`button-text ${-1!==o.indexOf(e.name)&&"selected"}`,onClick:()=>h(e.name),active:-1!==o.indexOf(e.name)},e.name)))),"line"===e&&a.createElement("div",{className:"control-wrapper",title:ge.lineDimensions},a.createElement("div",null,a.createElement(oe.a,null,"Metrics")),a.createElement(x,{vertical:!0},r.map(e=>a.createElement(Y.a,{key:`metrics-select-${e.name}`,className:`button-text ${-1!==l.indexOf(e.name)&&"selected"}`,onClick:()=>d(e.name),active:-1!==l.indexOf(e.name)},e.name))))),a.createElement(H.a,null),a.createElement(H.b,null))},$e=r(91);const Pe=e=>a.createElement($e.h,{width:16,height:16,viewBox:"0 0 16 16",outerProps:e},a.createElement("title",null,"Summary Diagram"),a.createElement("path",{fill:"var(--theme-app-bg)",stroke:"var(--theme-app-fg)",d:"M 9.2300893,12.746467 15.329337,12.746467 M 0.73981357,15.376296 6.8390612,15.376296 M 3.9346579,0.6634694 3.9346579,15.376296 M 0.73981357,0.6634694 6.8390612,0.6634694 M 12.424932,1.5163867 12.424932,12.817543 M 9.2300893,1.5163867 15.329337,1.5163867 M 9.3149176,3.8522966 15.454941,3.8522966 15.454941,10.067428 9.3149176,10.067428 Z M 0.63101533,5.4042547 6.771038,5.4042547 6.771038,13.040916 0.63101533,13.040916 Z"})),Fe=e=>a.createElement($e.h,{width:16,height:16,viewBox:"0 0 16 16",outerProps:e},a.createElement("title",null,"Dendrogram"),a.createElement("path",{fill:"var(--theme-app-bg)",stroke:"var(--theme-app-fg)",d:"M 5.3462352,16.86934 5.3462352,11.568531 M 5.0378073,11.186463 10.665375,16.453304 M 5.5794816,11.049276 -0.04808655,16.316116 M 10.903757,11.840357 10.903757,6.5395482 M 10.722225,5.9958343 16.349791,11.262675 M 10.758529,6.1997119 5.1309613,11.466552 M 5.3851096,6.1997401 5.3851096,0.06818774 M 5.3488028,0.96685111 10.976372,6.2336914 M 5.3851095,0.89889187 -0.24245868,6.1657322"})),Ae=e=>a.createElement($e.h,{width:16,height:16,viewBox:"0 0 16 16",outerProps:e},a.createElement("title",null,"Network"),a.createElement("path",{fill:"var(--theme-app-bg)",stroke:"var(--theme-app-fg)",d:"M 12.272948,3.9756652 9.2580839,6.8311579 M 3.7415227,3.9107679 6.435657,6.5066704 M 3.9981069,12.087859 6.6280954,9.6866496 M 12.208802,12.217654 9.0656456,9.556855 M 0.58721146,13.461599 A 2.0038971,2.0273734 0 0 0 2.591109,15.488973 2.0038971,2.0273734 0 0 0 4.5950056,13.461599 2.0038971,2.0273734 0 0 0 2.591109,11.434226 2.0038971,2.0273734 0 0 0 0.58721146,13.461599 Z M 11.483612,2.5370283 A 2.0038971,2.0273734 0 0 0 13.487509,4.5644013 2.0038971,2.0273734 0 0 0 15.491407,2.5370283 2.0038971,2.0273734 0 0 0 13.487509,0.50965432 2.0038971,2.0273734 0 0 0 11.483612,2.5370283 Z M 15.491407,13.461599 A 2.0038971,2.0273734 0 0 1 13.487509,15.488973 2.0038971,2.0273734 0 0 1 11.483612,13.461599 2.0038971,2.0273734 0 0 1 13.487509,11.434226 2.0038971,2.0273734 0 0 1 15.491407,13.461599 Z M 9.9298938,8.1089002 A 2.0038971,2.0273734 0 0 1 7.9259965,10.136275 2.0038971,2.0273734 0 0 1 5.9220989,8.1089002 2.0038971,2.0273734 0 0 1 7.9259965,6.0815273 2.0038971,2.0273734 0 0 1 9.9298938,8.1089002 Z M 4.5950056,2.5370283 A 2.0038971,2.0273734 0 0 1 2.591109,4.5644013 2.0038971,2.0273734 0 0 1 0.58721146,2.5370283 2.0038971,2.0273734 0 0 1 2.591109,0.50965432 2.0038971,2.0273734 0 0 1 4.5950056,2.5370283 Z"})),Ne=e=>a.createElement($e.h,{width:16,height:16,viewBox:"0 0 16 16",outerProps:e},a.createElement("title",null,"Scatterplot"),a.createElement("path",{fill:"var(--theme-app-bg)",stroke:"var(--theme-app-fg)",d:"M 6.2333524,7.1483631 A 2.1883047,2.1883047 0 0 1 4.0450478,9.3366678 2.1883047,2.1883047 0 0 1 1.8567431,7.1483631 2.1883047,2.1883047 0 0 1 4.0450478,4.9600585 2.1883047,2.1883047 0 0 1 6.2333524,7.1483631 Z M 12.201456,4.0316868 A 2.1883047,2.1883047 0 0 1 10.013151,6.2199914 2.1883047,2.1883047 0 0 1 7.8248465,4.0316868 2.1883047,2.1883047 0 0 1 10.013151,1.8433821 2.1883047,2.1883047 0 0 1 12.201456,4.0316868 Z M 14.787634,11.45866 A 2.1883047,2.1883047 0 0 1 12.599329,13.646965 2.1883047,2.1883047 0 0 1 10.411024,11.45866 2.1883047,2.1883047 0 0 1 12.599329,9.2703555 2.1883047,2.1883047 0 0 1 14.787634,11.45866 Z M 0.06631226,-0.01336003 0.06631226,16.100519 16.113879,16.100519"})),Be=e=>a.createElement($e.h,{width:16,height:16,viewBox:"0 0 16 16",outerProps:e},a.createElement("title",null,"Line Chart"),a.createElement("path",{fill:"var(--theme-app-bg)",stroke:"var(--theme-app-fg)",d:"M 1.98856,5.3983376 3.9789255,1.5485605 6.8981275,9.2481137 10.215403,6.6815963 15.257662,12.071285 M 0.46261318,0.00862976 0.46261318,15.600225 16.518227,15.600225"})),Le=e=>a.createElement($e.h,{width:16,height:16,viewBox:"0 0 16 16",outerProps:e},a.createElement("title",null,"Hexbin"),a.createElement("path",{fill:"var(--theme-app-bg)",stroke:"var(--theme-app-fg)",d:"M 7.6646201,7.248835 10.200286,8.7365914 12.71271,7.2956277 12.71271,4.2993354 10.200286,2.8583717 7.6481891,4.3220885 Z M 2.5260861,7.248835 5.0617524,8.7365914 7.5741798,7.2956277 7.5741798,4.2993354 5.0617524,2.8583717 2.509655,4.3220885 Z M 10.151008,11.430063 12.686686,12.917818 15.199098,11.476854 15.199098,8.4805611 12.686686,7.0395985 10.134577,8.5033165 Z M 5.0124743,11.430063 7.5481406,12.917818 10.060567,11.476854 10.060567,8.4805611 7.5481406,7.0395985 4.9960421,8.5033165 Z M 0.59322509,-0.02976587 0.59322509,16.053058 16.562547,16.008864"})),Ge=e=>a.createElement($e.h,{width:16,height:16,viewBox:"0 0 16 16",outerProps:e},a.createElement("title",null,"Bar Chart"),a.createElement("path",{fill:"var(--theme-app-bg)",stroke:"var(--theme-app-fg)",d:"M 11.58591,8.3025699 15.255735,8.3025699 15.255735,15.691481 11.58591,15.691481 Z M 6.2401471,3.973457 9.9358173,3.973457 9.9358173,15.626376 6.2401471,15.626376 Z M 0.533269,0.53717705 4.6376139,0.53717705 4.6376139,15.583893 0.533269,15.583893 Z"})),Ke=e=>a.createElement($e.h,{width:16,height:16,viewBox:"0 0 16 16",outerProps:e},a.createElement("title",null,"Bar Chart"),a.createElement("path",{fill:"var(--theme-app-bg)",stroke:"var(--theme-app-fg)",d:"M 2.7232684,11.593098 8.8105743,9.8309837 14.417303,4.2242547 M 12.356336,0.72968704 15.29192,0.72968704 15.29192,8.4261754 12.356336,8.4261754 Z M 6.8447585,6.4156084 10.103282,6.4156084 10.103282,12.352066 6.8447585,12.352066 Z M 0.51572132,6.0114684 3.9294777,6.0114684 3.9294777,16.25395 0.51572132,16.25395 Z"}));class We extends a.Component{render(){const{message:e,onClick:t,children:r,selected:n}=this.props,{title:i=e}=this.props;let o={width:"32px",height:"32px",cursor:"pointer",color:"var(--theme-app-fg)",border:"1px solid var(--theme-app-fg)",backgroundColor:"var(--theme-app-bg)"};return n&&(o.border="1px outset #666",o.backgroundColor="#aaa"),a.createElement("button",{onClick:t,key:e,title:i,style:o},r)}}const Ze=({dimensions:e,setGrid:t,setView:r,currentView:n})=>a.createElement("div",{style:{display:"flex",flexFlow:"column nowrap",zIndex:1,padding:"5px"},className:"dx-button-bar"},a.createElement(We,{title:pe,onClick:t,message:"Data Table",selected:!1},a.createElement($e.d,null)),e.length>0&&a.createElement(We,{title:se,onClick:()=>r("bar"),selected:"bar"===n,message:"Bar Graph"},a.createElement(Ge,null)),a.createElement(We,{title:de,onClick:()=>r("summary"),selected:"summary"===n,message:"Summary"},a.createElement(Pe,null)),a.createElement(We,{title:ce,onClick:()=>r("scatter"),selected:"scatter"===n,message:"Scatter Plot"},a.createElement(Ne,null)),a.createElement(We,{title:he,onClick:()=>r("hexbin"),selected:"hexbin"===n,message:"Area Plot"},a.createElement(Le,null)),e.length>1&&a.createElement(We,{title:me,onClick:()=>r("network"),selected:"network"===n,message:"Network"},a.createElement(Ae,null)),e.length>0&&a.createElement(We,{title:ue,onClick:()=>r("hierarchy"),selected:"hierarchy"===n,message:"Hierarchy"},a.createElement(Fe,null)),e.length>0&&a.createElement(We,{title:be,onClick:()=>r("parallel"),selected:"parallel"===n,message:"Parallel Coordinates"},a.createElement(Ke,null)),a.createElement(We,{title:le,onClick:()=>r("line"),selected:"line"===n,message:"Line Graph"},a.createElement(Be,null))),De="application/vnd.dataresource+json",Ie=({view:e,lineType:t,areaType:r,selectedDimensions:a,selectedMetrics:n,pieceType:i,summaryType:o,networkType:l,hierarchyType:s,chart:c})=>`${e}-${t}-${r}-${a.join(",")}-${n.join(",")}-${i}-${o}-${l}-${s}-${JSON.stringify(c)}`,Ye=({metadata:e})=>{const t=e&&e.sampled?a.createElement("span",null,a.createElement("b",null,"NOTE:")," This data is sampled"):null;return a.createElement("div",{style:{fontFamily:"Source Sans Pro, Helvetica Neue, Helvetica, Arial, sans-serif"}},t?a.createElement("div",{style:{backgroundColor:"#cce",padding:"10px",paddingLeft:"20px"}},t):null)},Xe=s.c.div`
  width: "calc(100vw - 200px)";
  .html-legend-item {
    color: var(--theme-app-fg);
  }

  .tick > path {
    stroke: lightgray;
  }

  .axis-labels,
  .ordinal-labels {
    fill: var(--theme-app-fg);
    font-size: 14px;
  }

  path.connector,
  path.connector-end {
    stroke: var(--theme-app-fg);
  }

  path.connector-end {
    fill: var(--theme-app-fg);
  }

  text.annotation-note-label,
  text.legend-title,
  .legend-item text {
    fill: var(--theme-app-fg);
    stroke: none;
  }

  .xyframe-area > path {
    stroke: var(--theme-app-fg);
  }

  .axis-baseline {
    stroke-opacity: 0.25;
    stroke: var(--theme-app-fg);
  }
  circle.frame-hover {
    fill: none;
    stroke: gray;
  }
  .rect {
    stroke: green;
    stroke-width: 5px;
    stroke-opacity: 0.5;
  }
  rect.selection {
    opacity: 0.5;
  }
`;class He extends a.Component{constructor(e){super(e),this.updateChart=(e=>{const{view:t,dimensions:r,metrics:n,chart:i,lineType:o,areaType:l,selectedDimensions:s,selectedMetrics:c,pieceType:p,summaryType:m,networkType:d,hierarchyType:h,colors:b,primaryKey:u,data:g}=Object.assign({},this.state,e),{data:y,height:x,onMetadataChange:f}=this.props,{Frame:k,chartGenerator:E}=K[t],v=Ie({view:t,lineType:o,areaType:l,selectedDimensions:s,selectedMetrics:c,pieceType:p,summaryType:m,networkType:d,hierarchyType:h,chart:i}),w=E(g,y.schema,{metrics:n,dimensions:r,chart:i,colors:b,height:x,lineType:o,areaType:l,selectedDimensions:s,selectedMetrics:c,pieceType:p,summaryType:m,networkType:d,hierarchyType:h,primaryKey:u,setColor:this.setColor}),T=a.createElement(Xe,null,a.createElement(k,Object.assign({responsiveWidth:!0,size:[500,300]},w)),a.createElement(ze,Object.assign({},{data:g,view:t,chart:i,metrics:n,dimensions:r,selectedDimensions:s,selectedMetrics:c,hierarchyType:h,summaryType:m,networkType:d,updateChart:this.updateChart,updateDimensions:this.updateDimensions,setLineType:this.setLineType,updateMetrics:this.updateMetrics,lineType:o,setAreaType:this.setAreaType,areaType:l})));f&&f(Object.assign({},this.props.metadata,{dx:{view:t,lineType:o,areaType:l,selectedDimensions:s,selectedMetrics:c,pieceType:p,summaryType:m,networkType:d,hierarchyType:h,colors:b,chart:i}})),this.setState(t=>Object.assign({},e,{displayChart:Object.assign({},t.displayChart,{[v]:T})}))}),this.setView=(e=>{this.updateChart({view:e})}),this.setGrid=(()=>{this.setState({view:"grid"})}),this.setColor=(e=>{this.updateChart({colors:e})}),this.setLineType=(e=>{this.updateChart({lineType:e})}),this.setAreaType=(e=>{this.updateChart({areaType:e})}),this.updateDimensions=(e=>{const t=this.state.selectedDimensions,r=-1===t.indexOf(e)?[...t,e]:t.filter(t=>t!==e);this.updateChart({selectedDimensions:r})}),this.updateMetrics=(e=>{const t=this.state.selectedMetrics,r=-1===t.indexOf(e)?[...t,e]:t.filter(t=>t!==e);this.updateChart({selectedMetrics:r})});const{metadata:t,initialView:r}=e,i=t.dx||{},o=i.chart||{},{fields:l=[],primaryKey:s=[]}=e.data.schema,c=l.filter(e=>"string"===e.type||"boolean"===e.type||"datetime"===e.type),p=e.data.data.map(e=>{const t=Object.assign({},e);return l.forEach(e=>{"datetime"===e.type&&(t[e.name]=new Date(t[e.name]))}),t}),m=l.filter(e=>"integer"===e.type||"number"===e.type||"datetime"===e.type).filter(e=>!s.find(t=>t===e.name));this.state=Object.assign({view:r,lineType:"line",areaType:"hexbin",selectedDimensions:[],selectedMetrics:[],pieceType:"bar",summaryType:"violin",networkType:"force",hierarchyType:"dendrogram",dimensions:c,metrics:m,colors:n,chart:Object.assign({metric1:m[0]&&m[0].name||"none",metric2:m[1]&&m[1].name||"none",metric3:"none",dim1:c[0]&&c[0].name||"none",dim2:c[1]&&c[1].name||"none",dim3:"none",timeseriesSort:"array-order",networkLabel:"none"},o),displayChart:{},primaryKey:s,data:p},i)}componentDidMount(){"grid"!==this.state.view&&this.updateChart(this.state)}render(){const{view:e,dimensions:t,chart:r,lineType:n,areaType:i,selectedDimensions:o,selectedMetrics:l,pieceType:s,summaryType:c,networkType:p,hierarchyType:m}=this.state;let d=null;if("grid"===e)d=a.createElement(ae,Object.assign({},this.props));else if(["line","scatter","bar","network","summary","hierarchy","hexbin","parallel"].includes(e)){const t=Ie({view:e,lineType:n,areaType:i,selectedDimensions:o,selectedMetrics:l,pieceType:s,summaryType:c,networkType:p,hierarchyType:m,chart:r});d=this.state.displayChart[t]}return a.createElement("div",null,a.createElement(Ye,{metadata:this.props.metadata}),a.createElement("div",{style:{display:"flex",flexFlow:"row nowrap",width:"100%"}},a.createElement("div",{style:{flex:"1"}},d),a.createElement(Ze,{dimensions:t,setGrid:this.setGrid,setView:this.setView,currentView:e})))}}He.MIMETYPE=De,He.defaultProps={metadata:{dx:{}},height:500,mediaType:De,initialView:"grid"};t.default=He}}]);