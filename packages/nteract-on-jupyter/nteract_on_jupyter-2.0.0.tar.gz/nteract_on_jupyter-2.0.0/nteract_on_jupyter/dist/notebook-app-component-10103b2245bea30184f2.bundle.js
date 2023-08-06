(window.webpackJsonp=window.webpackJsonp||[]).push([[5],{1015:function(e,t){},1260:function(e,t,o){"use strict";var r=o(0),n=o(177),i=o(3),s=o(340);const l=({componentStack:e,error:t})=>r.createElement("div",{style:{backgroundColor:"ghostwhite",color:"black",fontWeight:600,display:"block",padding:"10px",marginBottom:"20px"}},r.createElement("h3",null," Error: ",t.toString()),r.createElement("details",null,r.createElement("summary",null,"stack trace"),r.createElement("pre",null,e)));class a extends r.Component{constructor(e){super(e),this.state={error:null,info:null}}componentDidCatch(e,t){this.setState({error:e,info:t})}render(){if(this.state.error)return r.createElement(l,{componentStack:this.state.info?this.state.info.componentStack:"",error:this.state.error});const e=Object(n.b)(this.props.bundle,this.props.displayOrder,this.props.transforms);if(!e)return null;const t=this.props.transforms[e],o=this.props.bundle[e],i=this.props.metadata[e];return r.createElement(t,{data:o,metadata:i,theme:this.props.theme,models:this.props.models,channels:this.props.channels,onMetadataChange:t=>this.props.onMetadataChange&&this.props.onMetadataChange(Object.assign({},this.props.metadata,{[e]:t}))})}}a.defaultProps={transforms:n.c,displayOrder:n.a,theme:"light",metadata:{},bundle:{},models:{}};const c="nteract-display-area-";class d extends r.Component{shouldComponentUpdate(e){return e.output!==this.props.output||e.displayOrder!==this.props.displayOrder||e.transforms!==this.props.transforms||e.theme!==this.props.theme||e.models!==this.props.models||e.channels!==this.props.channels}render(){let e=this.props.output,t=this.props.models;switch(Object(i.isImmutable)(e)&&(e=e.toJS()),Object(i.isImmutable)(t)&&(t=t.toJS()),e.output_type){case"execute_result":case"display_data":{const o=e.data,n=e.metadata,i=this.props.onMetadataChange&&this.props.onMetadataChange.bind(null,this.props.index);return r.createElement(a,{bundle:o,metadata:n,displayOrder:this.props.displayOrder,transforms:this.props.transforms,theme:this.props.theme,models:t,channels:this.props.channels,onMetadataChange:i})}case"stream":{const t=e.text,o=e.name;switch(o){case"stdout":case"stderr":return r.createElement(s.a,{linkify:!1,className:c+o},t);default:return null}}case"error":{const t=e.traceback;return t?r.createElement(s.a,{linkify:!1,className:c+"traceback"},t.join("\n")):r.createElement(s.a,{linkify:!1,className:c+"traceback"},`${e.ename}: ${e.evalue}`)}default:return null}}}d.defaultProps={models:{},theme:"light",transforms:n.c,displayOrder:n.a,metadata:{}};var p=function(e,t){var o={};for(var r in e)Object.prototype.hasOwnProperty.call(e,r)&&t.indexOf(r)<0&&(o[r]=e[r]);if(null!=e&&"function"==typeof Object.getOwnPropertySymbols){var n=0;for(r=Object.getOwnPropertySymbols(e);n<r.length;n++)t.indexOf(r[n])<0&&(o[r[n]]=e[r[n]])}return o};const u=600;(class extends r.PureComponent{render(){const e=this.props,{isHidden:t,outputs:o}=e,n=p(e,["isHidden","outputs"]);return t?null:r.createElement("div",{className:"cell_display",style:{maxHeight:n.expanded?"100%":`${u}px`,overflowY:"auto"}},o?o.map((e,t)=>r.createElement(d,Object.assign({key:t,index:t,output:e},n))):null)}}).defaultProps={transforms:n.c,displayOrder:n.a,isHidden:!1,expanded:!1,theme:"light",models:Object(i.Map)()},o.d(t,"b",function(){return a}),o.d(t,"a",function(){return d})},1263:function(e,t,o){"use strict";var r=o(0),n=o(27),i=o(2),s=o(66),l=o(9);const a=l.c.div`
  z-index: 10000;
  display: inline-block;
`;a.displayName="DropdownDiv";class c extends r.Component{constructor(e){super(e),this.state={menuHidden:!0}}render(){return r.createElement(a,null,r.Children.map(this.props.children,e=>{const t=e;return Object(s.areComponentsEqual)(t.type,p)?r.cloneElement(t,{onClick:()=>{this.setState({menuHidden:!this.state.menuHidden})}}):Object(s.areComponentsEqual)(t.type,m)?this.state.menuHidden?null:r.cloneElement(t,{onItemClick:()=>{this.setState({menuHidden:!0})}}):e}))}}const d=l.c.div`
  user-select: none;
  margin: 0px;
  padding: 0px;
`;d.displayName="DropdownTriggerDiv";class p extends r.Component{render(){return r.createElement(d,{onClick:this.props.onClick},this.props.children)}}const u=l.c.div`
  user-select: none;
  margin: 0px;
  padding: 0px;

  width: 200px;

  opacity: 1;
  position: absolute;
  top: 0.2em;
  right: 0;
  border-style: none;
  padding: 0;
  font-family: var(--nt-font-family-normal);
  font-size: var(--nt-font-size-m);
  line-height: 1.5;
  margin: 20px 0;
  background-color: var(--theme-cell-menu-bg);

  ul {
    list-style: none;
    text-align: left;
    padding: 0;
    margin: 0;
    opacity: 1;
  }

  ul li {
    padding: 0.5rem;
  }

  ul li:hover {
    background-color: var(--theme-cell-menu-bg-hover, #e2dfe3);
    cursor: pointer;
  }
`;u.displayName="DropdownContentDiv";class m extends r.Component{render(){return r.createElement(u,null,r.createElement("ul",null,r.Children.map(this.props.children,e=>{const t=e;return r.cloneElement(t,{onClick:e=>{t.props.onClick(e),this.props.onItemClick(e)}})})))}}m.defaultProps={onItemClick:()=>{}};var h=o(91);o.d(t,"a",function(){return b});const f=l.c.div`
  background-color: var(--theme-cell-toolbar-bg);
  opacity: 0.4;
  transition: opacity 0.4s;

  & > div {
    display: inline-block;
  }

  :hover {
    opacity: 1;
  }

  button {
    display: inline-block;

    width: 22px;
    height: 20px;
    padding: 0px 4px;

    text-align: center;

    border: none;
    outline: none;
    background: none;
  }

  span {
    font-size: 15px;
    line-height: 1;
    color: var(--theme-cell-toolbar-fg);
  }

  button span:hover {
    color: var(--theme-cell-toolbar-fg-hover);
  }

  .octicon {
    transition: color 0.5s;
  }

  span.spacer {
    display: inline-block;
    vertical-align: middle;
    margin: 1px 5px 3px 5px;
    height: 11px;
  }
`,b=l.c.div`
  z-index: 9999;
  display: ${e=>e.sourceHidden?"block":"none"};
  position: absolute;
  top: 0px;
  right: 0px;
  height: 34px;

  /* Set the left padding to 50px to give users extra room to move their
              mouse to the toolbar without causing the cell to go out of focus and thus
              hide the toolbar before they get there. */
  padding: 0px 0px 0px 50px;
`;class g extends r.Component{render(){const{type:e,executeCell:t,deleteCell:o,sourceHidden:n}=this.props;return r.createElement(b,{sourceHidden:n},r.createElement(f,null,"markdown"!==e&&r.createElement("button",{onClick:t,title:"execute cell",className:"executeButton"},r.createElement("span",{className:"octicon"},r.createElement(h.j,null))),r.createElement(c,null,r.createElement(p,null,r.createElement("button",{title:"show additional actions"},r.createElement("span",{className:"octicon toggle-menu"},r.createElement(h.b,null)))),"code"===e?r.createElement(m,null,r.createElement("li",{onClick:this.props.clearOutputs,className:"clearOutput",role:"option","aria-selected":"false",tabIndex:0},r.createElement("a",null,"Clear Cell Output")),r.createElement("li",{onClick:this.props.toggleCellInputVisibility,className:"inputVisibility",role:"option","aria-selected":"false",tabIndex:0},r.createElement("a",null,"Toggle Input Visibility")),r.createElement("li",{onClick:this.props.toggleCellOutputVisibility,className:"outputVisibility",role:"option","aria-selected":"false",tabIndex:0},r.createElement("a",null,"Toggle Output Visibility")),r.createElement("li",{onClick:this.props.toggleOutputExpansion,className:"outputExpanded",role:"option","aria-selected":"false",tabIndex:0},r.createElement("a",null,"Toggle Expanded Output")),r.createElement("li",{onClick:this.props.toggleParameterCell,role:"option","aria-selected":"false",tabIndex:0},r.createElement("a",null,"Toggle Parameter Cell")),r.createElement("li",{onClick:this.props.changeCellType,className:"changeType",role:"option","aria-selected":"false",tabIndex:0},r.createElement("a",null,"Convert to Markdown Cell"))):r.createElement(m,null,r.createElement("li",{onClick:this.props.changeCellType,className:"changeType",role:"option","aria-selected":"false",tabIndex:0},r.createElement("a",null,"Convert to Code Cell")))),r.createElement("span",{className:"spacer"}),r.createElement("button",{onClick:o,title:"delete cell",className:"deleteButton"},r.createElement("span",{className:"octicon"},r.createElement(h.i,null)))))}}g.defaultProps={type:"code"};t.b=Object(n.b)(null,(e,{id:t,type:o,contentRef:r})=>({toggleParameterCell:()=>e(i.toggleParameterCell({id:t,contentRef:r})),deleteCell:()=>e(i.deleteCell({id:t,contentRef:r})),executeCell:()=>e(i.executeCell({id:t,contentRef:r})),clearOutputs:()=>e(i.clearOutputs({id:t,contentRef:r})),toggleCellOutputVisibility:()=>e(i.toggleCellOutputVisibility({id:t,contentRef:r})),toggleCellInputVisibility:()=>e(i.toggleCellInputVisibility({id:t,contentRef:r})),changeCellType:()=>e(i.changeCellType({id:t,to:"markdown"===o?"code":"markdown",contentRef:r})),toggleOutputExpansion:()=>e(i.toggleOutputExpansion({id:t,contentRef:r}))}))(g)},1265:function(e,t,o){"use strict";(function(e){var r=o(3),n=o(0),i=o(8),s=o(167),l=o(1160),a=o(1325),c=o.n(a),d=o(27),p=o(1260),u=o(177),m=o(1337),h=o(1338),f=o(1339),b=o(1354),g=o(1781),C=o(1263),x=o(1372),v=o(9);const k={dark:v.a`
    :root {
      ${s.i.dark}
    }`,light:v.a`
    :root {
      ${s.i.light}
    }`};const y=Object(v.c)(s.a)`
  /*
   * Show the cell-toolbar-mask if hovering on cell,
   * cell was the last clicked (has .focused class).
   */
  &:hover ${C.a} {
    display: block;
  }
  & ${C.a} {
    ${e=>e.isSelected?"display: block;":""}
  }
`;y.displayName="Cell";const w={lineWrapping:!0,mode:{name:"gfm",tokenTypeOverrides:{emoji:"emoji"}}},E={lineWrapping:!0,mode:{name:"text/plain",tokenTypeOverrides:{emoji:"emoji"}}},M=v.c.div`
  background-color: darkblue;
  color: ghostwhite;
  padding: 9px 16px;

  font-size: 12px;
  line-height: 20px;
`;M.displayName="CellBanner";const O=Object(d.b)((e,{id:t,contentRef:o})=>{const n=i.q.model(e,{contentRef:o});if(!n||"notebook"!==n.type)throw new Error("Cell components should not be used with non-notebook models");const s=i.q.notebook.cellById(n,{id:t});if(!s)throw new Error("cell not found inside cell map");const l=s.get("cell_type"),a=s.get("outputs",r.List()),c="code"===l&&(s.getIn(["metadata","inputHidden"])||s.getIn(["metadata","hide_input"]))||!1,d="code"===l&&(0===a.size||s.getIn(["metadata","outputHidden"])),p="code"===l&&s.getIn(["metadata","outputExpanded"]),u=s.getIn(["metadata","tags"])||r.Set(),m=n.getIn(["cellPagers",t])||r.List(),h=(s.getIn(["metadata"])||r.Map()).toJS(),f=i.q.currentKernelRef(e);let b;if(f){const t=i.q.kernel(e,{kernelRef:f});t&&(b=t.channels)}return{contentRef:o,channels:b,cellType:l,tags:u,source:s.get("source",""),theme:i.q.userTheme(e),executionCount:s.get("execution_count",null),outputs:a,models:i.q.models(e),pager:m,cellFocused:n.cellFocused===t,editorFocused:n.editorFocused===t,sourceHidden:c,outputHidden:d,outputExpanded:p,cellStatus:n.transient.getIn(["cellMap",t,"status"]),metadata:h}},(e,{id:t,contentRef:o})=>({selectCell:()=>e(i.a.focusCell({id:t,contentRef:o})),focusEditor:()=>e(i.a.focusCellEditor({id:t,contentRef:o})),unfocusEditor:()=>e(i.a.focusCellEditor({id:void 0,contentRef:o})),focusAboveCell:()=>{e(i.a.focusPreviousCell({id:t,contentRef:o})),e(i.a.focusPreviousCellEditor({id:t,contentRef:o}))},focusBelowCell:()=>{e(i.a.focusNextCell({id:t,createCellIfUndefined:!0,contentRef:o})),e(i.a.focusNextCellEditor({id:t,contentRef:o}))},updateOutputMetadata:(r,n)=>{e(i.a.updateOutputMetadata({id:t,contentRef:o,metadata:n,index:r}))}}))(class extends n.PureComponent{render(){const{cellFocused:e,cellStatus:t,cellType:o,editorFocused:i,focusAboveCell:l,focusBelowCell:a,focusEditor:c,id:d,tags:u,selectCell:m,unfocusEditor:h,contentRef:f,sourceHidden:v,metadata:k}=this.props,O="busy"===t,R="queued"===t;let S=null;switch(o){case"code":S=n.createElement(n.Fragment,null,n.createElement(s.c,{hidden:this.props.sourceHidden},n.createElement(s.f,{counter:this.props.executionCount,running:O,queued:R}),n.createElement(s.h,null,n.createElement(g.a,{tip:!0,completion:!0,id:d,contentRef:f,value:this.props.source,cellFocused:e,editorFocused:i,theme:this.props.theme,focusAbove:l,focusBelow:a,options:{mode:r.isImmutable(this.props.codeMirrorMode)?this.props.codeMirrorMode.toJS():this.props.codeMirrorMode}}))),n.createElement(s.e,null,this.props.pager.map((e,t)=>n.createElement(p.b,{metadata:{expanded:!0},className:"pager",displayOrder:this.props.displayOrder,transforms:this.props.transforms,bundle:e,theme:this.props.theme,key:t}))),n.createElement(s.d,{hidden:this.props.outputHidden,expanded:this.props.outputExpanded},this.props.outputs.map((e,t)=>n.createElement(p.a,{key:t,output:e,displayOrder:this.props.displayOrder,transforms:this.props.transforms,theme:this.props.theme,models:this.props.models,channels:this.props.channels,onMetadataChange:this.props.updateOutputMetadata,index:t,metadata:k}))));break;case"markdown":S=n.createElement(b.a,{focusAbove:l,focusBelow:a,focusEditor:c,cellFocused:e,editorFocused:i,unfocusEditor:h,source:this.props.source},n.createElement(s.h,null,n.createElement(g.a,{id:d,value:this.props.source,theme:this.props.theme,focusAbove:l,focusBelow:a,cellFocused:e,editorFocused:i,contentRef:f,options:w})));break;case"raw":S=n.createElement(s.h,null,n.createElement(g.a,{id:d,value:this.props.source,theme:this.props.theme,focusAbove:l,focusBelow:a,cellFocused:e,editorFocused:i,contentRef:f,options:E}));break;default:S=n.createElement("pre",null,this.props.source)}return n.createElement(x.a,{focused:e,onClick:m},n.createElement(y,{isSelected:e},u.has("parameters")?n.createElement(M,null,"Papermill - Parametrized"):null,u.has("default parameters")?n.createElement(M,null,"Papermill - Default Parameters"):null,n.createElement(C.b,{type:o,sourceHidden:v,id:d,contentRef:f}),S))}}),R=v.c.div`
  padding-top: var(--nt-spacing-m, 10px);
  padding-left: var(--nt-spacing-m, 10px);
  padding-right: var(--nt-spacing-m, 10px);
`;class S extends n.PureComponent{constructor(e){super(e),this.createCellElement=this.createCellElement.bind(this),this.keyDown=this.keyDown.bind(this),this.renderCell=this.renderCell.bind(this)}componentDidMount(){document.addEventListener("keydown",this.keyDown)}componentWillUnmount(){document.removeEventListener("keydown",this.keyDown)}keyDown(t){if(13!==t.keyCode)return;const{executeFocusedCell:o,focusNextCell:r,focusNextCellEditor:n,contentRef:i}=this.props;let s=t.ctrlKey;"darwin"===e.platform&&(s=(t.metaKey||t.ctrlKey)&&!(t.metaKey&&t.ctrlKey)),(t.shiftKey||s)&&!(t.shiftKey&&s)&&(t.preventDefault(),o({contentRef:i}),t.shiftKey&&(r({id:void 0,createCellIfUndefined:!0,contentRef:i}),n({id:void 0,contentRef:i})))}renderCell(e){const{contentRef:t}=this.props;return n.createElement(O,{id:e,transforms:this.props.transforms,displayOrder:this.props.displayOrder,codeMirrorMode:this.props.codeMirrorMode,contentRef:t})}createCellElement(e){const{moveCell:t,focusCell:o,contentRef:r}=this.props;return n.createElement("div",{className:"cell-container",key:`cell-container-${e}`},n.createElement(m.a,{moveCell:t,id:e,focusCell:o,contentRef:r},this.renderCell(e)),n.createElement(h.a,{key:`creator-${e}`,id:e,above:!1,contentRef:r}))}render(){return n.createElement(n.Fragment,null,n.createElement(R,null,n.createElement(h.a,{id:this.props.cellOrder.get(0),above:!0,contentRef:this.props.contentRef}),this.props.cellOrder.map(this.createCellElement)),n.createElement(f.a,{contentRef:this.props.contentRef,kernelRef:this.props.kernelRef}),function(e){switch(e){case"dark":return n.createElement(k.dark,null);case"light":default:return n.createElement(k.light,null)}}(this.props.theme))}}S.defaultProps={theme:"light",displayOrder:u.c,transforms:u.a};const j=Object(l.DragDropContext)(c.a)(S);t.a=Object(d.b)((e,t)=>{const o=t.contentRef;if(!o)throw new Error("<Notebook /> has to have a contentRef");const n=i.q.content(e,{contentRef:o}),s=i.q.model(e,{contentRef:o});if(!s||!n)throw new Error("<Notebook /> has to have content & model that are notebook types");if("dummy"===s.type||"unknown"===s.type)return{theme:i.q.userTheme(e),cellOrder:r.List(),transforms:t.transforms||u.c,displayOrder:t.displayOrder||u.a,codeMirrorMode:r.Map({name:"text/plain"}),kernelRef:null,contentRef:o};if("notebook"!==s.type)throw new Error("<Notebook /> has to have content & model that are notebook types");const l=i.q.currentKernelRef(e)||t.kernelRef||s.kernelRef;let a=null;if(l){const t=i.q.kernel(e,{kernelRef:l});t&&(a=t.info)}const c=a?a.codemirrorMode:i.q.notebook.codeMirrorMode(s);return{theme:i.q.userTheme(e),cellOrder:i.q.notebook.cellOrder(s),transforms:t.transforms||u.c,displayOrder:t.displayOrder||u.a,codeMirrorMode:c,contentRef:o,kernelRef:l}},e=>({moveCell:t=>e(i.a.moveCell(t)),focusCell:t=>e(i.a.focusCell(t)),executeFocusedCell:t=>e(i.a.executeFocusedCell(t)),focusNextCell:t=>e(i.a.focusNextCell(t)),focusNextCellEditor:t=>e(i.a.focusNextCellEditor(t)),updateOutputMetadata:t=>e(i.a.updateOutputMetadata(t))}))(j)}).call(this,o(59))},1337:function(e,t,o){"use strict";var r=o(0),n=o(1160),i=o(9);const s=["data:image/png;base64,","iVBORw0KGgoAAAANSUhEUgAAADsAAAAzCAYAAAApdnDeAAAAAXNSR0IArs4c6QAA","AwNJREFUaAXtmlFL3EAUhe9MZptuoha3rLWgYC0W+lj/T3+26INvXbrI2oBdE9km","O9Nzxu1S0LI70AQScyFmDDfkfvdMZpNwlCCccwq7f21MaVM4FPtkU0o59RdoJBMx","WZINBg+DQWGKCAk+2kIKFh9JlSzLYVmOilEpR1Kh/iUbQFiNQTSbzWJrbYJximOJ","cSaulpVRoqh4K8JhjprIVJWqFlCpQNG51roYj8cLjJcGf5RMZWC1TYw1o2LxcEmy","0jeEo3ZFWVHIx0ji4eeKHFOx8l4sVVVZnBE6tWLHq7xO7FY86YpPeVjeo5y61tlR","JyhXEOQhF/lw6BGWixHvUWXVTpdgyUMu8q1h/ZJbqQhdiLsESx4FLvL9gcV6q3Cs","0liq2IHuBHjItYIV3rMvJnrYrkrdK9sr24EO9NO4AyI+i/CilOXbTi1xeXXFTyAS","GSOfzs42XmM+v5fJ5JvP29/fl8PDw43nhCbUpuzFxYXs7OxKmqZb1WQGkc/P80K+","T6dbnROaVJuyfPY+Pj7aup7h66HP/1Uu5O7u59bnhSTWpmxIEU3l9rBNdbrp6/TK","Nt3xpq7XK9tUp5u+Tm2/s/jYJdfX12LwBHVycrKRK89zmeJhYnZ7K3Fcz3e/2mDP","z7/waZEf8zaC+gSkKa3l4OBA3uztbXdOYFZtsKcfToNKSZNUPp6GnRN0AST3C1Ro","x9qS3yvbFqVC6+yVDe1YW/J7ZduiVGidvbKhHWtLfq9sW5QKrdMri9cxB6OFhQmO","TrDuBHjIRT5CEZZj0i7xOkYnWGeCPOQiHqC8lc/R60cLnNPuvjOkns7dk4t8/Jfv","s46mRlWqQiudxebVV3gAj7C9hXsmgZeztnfe/91YODEr3IoF/JY/sE2gbGaVLci3","hh0tRtWNvsm16JmNcOs6N9dW72LP7yOtWbEhjAUkZ+icoJ5HbE6+NSxMjKWe6cKb","GkUWgMwiFbXSlRpFkXelUlF4F70rVd7Bd4oZ/LL8xiDmtPV2Nwyf2zOlTfHERY7i","Haa1+w2+iFqx0aIgvgAAAABJRU5ErkJggg=="].join(""),l={beginDrag:e=>({id:e.id})},a=i.c.div.attrs({role:"presentation"})`
  position: absolute;
  z-index: 200;
  width: var(--prompt-width, 50px);
  height: 100%;
  cursor: move;
`,c=i.c.div`
  position: relative;
  padding: 10px;
  opacity: ${e=>e.isDragging?.25:1};
  border-top: ${e=>e.isOver&&e.hoverUpperHalf?"3px lightgray solid":"3px transparent solid"};
  border-bottom: ${e=>e.isOver&&!e.hoverUpperHalf?"3px lightgray solid":"3px transparent solid"};
`;function d(e,t,o){const r=o.getBoundingClientRect(),n=(r.bottom-r.top)/2;return t.getClientOffset().y-r.top<n}const p={drop(e,t,o){if(t){const r=d(0,t,o.el);e.moveCell({id:t.getItem().id,destinationId:e.id,above:r,contentRef:e.contentRef})}},hover(e,t,o){t&&o.setState({hoverUpperHalf:d(0,t,o.el)})}};const u=Object(n.DragSource)("CELL",l,function(e,t){return{connectDragSource:e.dragSource(),isDragging:t.isDragging(),connectDragPreview:e.dragPreview()}}),m=Object(n.DropTarget)("CELL",p,function(e,t){return{connectDropTarget:e.dropTarget(),isOver:t.isOver()}});t.a=u(m(class extends r.Component{constructor(){super(...arguments),this.state={hoverUpperHalf:!0},this.selectCell=(()=>{const{focusCell:e,id:t,contentRef:o}=this.props;e({id:t,contentRef:o})})}componentDidMount(){const e=this.props.connectDragPreview,t=new window.Image;t.src=s,t.onload=function(){e(t)}}render(){return this.props.connectDropTarget(r.createElement("div",null,r.createElement(c,{isDragging:this.props.isDragging,hoverUpperHalf:this.state.hoverUpperHalf,isOver:this.props.isOver,ref:e=>{this.el=e}},this.props.connectDragSource(r.createElement("div",null,r.createElement(a,{onClick:this.selectCell}))),this.props.children)))}}))},1338:function(e,t,o){"use strict";var r=o(0),n=o(27),i=o(91),s=o(2),l=o(9);const a=l.c.div`
  display: none;
  background: var(--theme-cell-creator-bg);
  box-shadow: 0 1px 2px 0 rgba(0, 0, 0, 0.5);
  pointer-events: all;
  position: relative;
  top: -5px;

  button {
    display: inline-block;

    width: 22px;
    height: 20px;
    padding: 0px 4px;

    text-align: center;

    border: none;
    outline: none;
    background: none;
  }

  button span {
    font-size: 15px;
    line-height: 1;

    color: var(--theme-cell-creator-fg);
  }

  button span:hover {
    color: var(--theme-cell-creator-fg-hover);
  }

  .octicon {
    transition: color 0.5s;
  }
`,c=l.c.div`
  display: block;
  position: relative;
  overflow: visible;
  height: 0px;
`,d=l.c.div`
  position: relative;
  overflow: visible;
  top: -10px;
  height: 60px;
  text-align: center;

  &:hover ${a} {
    display: inline-block;
  }
`;class p extends r.Component{constructor(){super(...arguments),this.createMarkdownCell=(()=>{this.props.createCell("markdown")}),this.createCodeCell=(()=>{this.props.createCell("code")})}render(){return r.createElement(c,null,r.createElement(d,null,r.createElement(a,null,r.createElement("button",{onClick:this.createMarkdownCell,title:"create text cell",className:"add-text-cell"},r.createElement("span",{className:"octicon"},r.createElement(i.g,null))),r.createElement("button",{onClick:this.createCodeCell,title:"create code cell",className:"add-code-cell"},r.createElement("span",{className:"octicon"},r.createElement(i.c,null))))))}}t.a=Object(n.b)(null,e=>({createCellAppend:t=>e(s.createCellAppend(t)),createCellAbove:t=>e(s.createCellAbove(t)),createCellBelow:t=>e(s.createCellBelow(t))}))(class extends r.Component{constructor(){super(...arguments),this.createCell=(e=>{const{above:t,createCellBelow:o,createCellAppend:r,createCellAbove:n,id:i,contentRef:s}=this.props;null!=i&&"string"==typeof i?t?n({cellType:e,id:i,contentRef:s}):o({cellType:e,id:i,source:"",contentRef:s}):r({cellType:e,contentRef:s})})}render(){return r.createElement(p,{above:this.props.above,createCell:this.createCell})}})},1339:function(e,t,o){"use strict";var r=o(0),n=o.n(r),i=o(27),s=o(1340),l=o.n(s),a=o(11),c=o(9);const d=c.c.div`
  float: left;
  display: block;
  padding-left: 10px;
`,p=c.c.div`
  float: right;
  padding-right: 10px;
  display: block;
`,u=c.c.div`
  position: fixed;
  bottom: 0;
  left: 0;
  width: 100%;
  font-size: 12px;
  line-height: 0.5em;
  background: var(--status-bar);
  z-index: 99;
`;t.a=Object(i.b)((e,t)=>{const{contentRef:o,kernelRef:r}=t,n=a.content(e,{contentRef:o}),i=null==r?a.kernel(e,{kernelRef:r}):null,s=n&&n.lastSaved?n.lastSaved:null,l=null!=i&&null!=i.status?i.status:"not connected";let c=" ";return"not connected"===l?c="no kernel":null!=i&&null!=i.kernelSpecName?c=i.kernelSpecName:null!=n&&"notebook"===n.type&&(c=a.notebook.displayName(n.model)||" "),{lastSaved:s,kernelStatus:l,kernelSpecDisplayName:c}})(class extends n.a.Component{shouldComponentUpdate(e){return this.props.lastSaved!==e.lastSaved||this.props.kernelStatus!==e.kernelStatus}render(){const e=this.props.kernelSpecDisplayName||"Loading...";return n.a.createElement(u,null,n.a.createElement(p,null,this.props.lastSaved?n.a.createElement("p",null," Last saved ",l()(this.props.lastSaved)," "):n.a.createElement("p",null," Not saved yet ")),n.a.createElement(d,null,n.a.createElement("p",null,e," | ",this.props.kernelStatus)))}})},1354:function(e,t,o){"use strict";o.d(t,"a",function(){return a});var r=o(0),n=o.n(r),i=o(354),s=o(167);const l=function(){};class a extends n.a.Component{constructor(e){super(e),this.state={view:!0},this.openEditor=this.openEditor.bind(this),this.editorKeyDown=this.editorKeyDown.bind(this),this.renderedKeyDown=this.renderedKeyDown.bind(this),this.closeEditor=this.closeEditor.bind(this)}componentDidMount(){this.updateFocus()}componentWillReceiveProps(e){this.setState({view:!e.editorFocused})}componentDidUpdate(){this.updateFocus()}updateFocus(){this.rendered&&this.state&&this.state.view&&this.props.cellFocused&&(this.rendered.focus(),this.props.editorFocused&&this.openEditor())}editorKeyDown(e){const t=e.shiftKey,o=e.ctrlKey;(t||o)&&"Enter"===e.key&&this.closeEditor()}closeEditor(){this.setState({view:!0}),this.props.unfocusEditor()}openEditor(){this.setState({view:!1}),this.props.focusEditor()}renderedKeyDown(e){const t=e.shiftKey,o=e.ctrlKey;if(!t&&!o||"Enter"!==e.key)switch(e.key){case"Enter":return this.openEditor(),void e.preventDefault();case"ArrowUp":this.props.focusAbove();break;case"ArrowDown":this.props.focusBelow()}else{if(this.state.view)return;this.closeEditor()}}render(){const e=this.props.source;return this.state&&this.state.view?n.a.createElement("div",{onDoubleClick:this.openEditor,onKeyDown:this.renderedKeyDown,ref:e=>{this.rendered=e},tabIndex:this.props.cellFocused?0:void 0,style:{outline:"none"}},n.a.createElement(s.d,null,n.a.createElement(i.a,{source:e||"*Empty markdown cell, double click me to add content.*"}))):n.a.createElement("div",{onKeyDown:this.editorKeyDown},n.a.createElement(s.c,null,n.a.createElement(s.g,null),this.props.children),n.a.createElement(s.d,{hidden:""===e},n.a.createElement(i.a,{source:e||"*Empty markdown cell, double click me to add content.*"})))}}a.defaultProps={cellFocused:!1,editorFocused:!1,focusAbove:l,focusBelow:l,focusEditor:l,unfocusEditor:l,source:""}},1371:function(e,t,o){"use strict";o.r(t);var r=o(853),n=o.n(r);o(1178),o(1176);n.a.defineMode("ipython",(e,t)=>{const o=Object.assign({},t,{name:"python",singleOperators:new RegExp("^[\\+\\-\\*/%&|@\\^~<>!\\?]"),identifiers:new RegExp("^[_A-Za-z¡-￿][_A-Za-z0-9¡-￿]*")});return n.a.getMode(e,o)},"python"),n.a.defineMIME("text/x-ipython","ipython")},1372:function(e,t,o){"use strict";o.d(t,"a",function(){return n});var r=o(0);class n extends r.Component{constructor(){super(...arguments),this.el=null}scrollIntoViewIfNeeded(e){const t=this.el&&this.el.parentElement&&this.el.parentElement.querySelector(":hover")===this.el;this.props.focused&&e!==this.props.focused&&!t&&(this.el&&"scrollIntoViewIfNeeded"in this.el?this.el.scrollIntoViewIfNeeded():this.el&&this.el.scrollIntoView())}componentDidUpdate(e){this.scrollIntoViewIfNeeded(e.focused)}componentDidMount(){this.scrollIntoViewIfNeeded()}render(){return r.createElement("div",{onClick:this.props.onClick,role:"presentation",ref:e=>{this.el=e}},this.props.children)}}},1781:function(e,t,o){"use strict";var r=o(27),n=o(2),i=o(11),s=o(83),l=o(0),a=o(13),c=o.n(a),d=o(1792),p=o(388),u=o(41),m=o(818),h=o(64),f=o(820),b=o(1804),g=o(1793),C=o(819),x=o(1794),v=o(45),k=o(821),y=o(1260);var w={8:"backspace",9:"tab",13:"enter",16:"shift",17:"ctrl",18:"alt",19:"pause",20:"capslock",27:"escape",32:"space",33:"pageup",34:"pagedown",35:"end",36:"home",37:"left",38:"up",39:"right",40:"down",45:"insert",46:"delete",91:"left window key",92:"right window key",93:"select",107:"add",109:"subtract",110:"decimal point",111:"divide",112:"f1",113:"f2",114:"f3",115:"f4",116:"f5",117:"f6",118:"f7",119:"f8",120:"f9",121:"f10",122:"f11",123:"f12",144:"numlock",145:"scrolllock",186:"semicolon",187:"equalsign",188:"comma",189:"dash",192:"graveaccent",220:"backslash",222:"quote"},E=o(10),M=o(822),O=o(825),R=o(25);let S=(e,t)=>{for(var o=e,r=0;r+1<t.length&&r<e;r++){var n=t.charCodeAt(r);if(n>=55296&&n<=56319){var i=t.charCodeAt(r+1);i>=56320&&i<=57343&&(o--,r++)}}return o},j=(e,t)=>{for(var o=e,r=0;r+1<t.length&&r<o;r++){var n=t.charCodeAt(r);if(n>=55296&&n<=56319){var i=t.charCodeAt(r+1);i>=56320&&i<=57343&&(o++,r++)}}return o};1==="𝐚".length&&(j=S=function(e,t){return e});const N=(e,t)=>t.pick();const F=e=>t=>{if(null!=(t.metadata||{})._jupyter_types_experimental)try{return((e,t,o)=>({to:o,from:o,list:t.map(t=>({text:t.text,to:e.posFromIndex(t.end),from:e.posFromIndex(t.start),type:t.type,render:(e,t,o)=>{const r=document.createElement("span"),n=document.createTextNode(o.text);r.className+="completion-type completion-type-"+o.type,r.setAttribute("title",o.type),e.appendChild(r),e.appendChild(n)}}))}))(e,t.metadata._jupyter_types_experimental,e.getCursor())}catch(e){console.error("Exprimental completion failed :",e)}let o=t.cursor_start,r=t.cursor_end;if(null===r)r=e.indexFromPos(e.getCursor()),null===o?o=r:o<0&&(o=r+o);else{const t=e.getValue();r=j(r,t),o=j(o,t)}return{list:t.matches.map(e=>({text:e,render:(e,t,o)=>e.appendChild(document.createTextNode(o.text))})),from:e.posFromIndex(o),to:e.posFromIndex(r)}};const A=(e,t)=>Object(R.createMessage)("complete_request",{content:{code:e,cursor_pos:t}});function D(e,t){const o=t.getCursor();let r=t.indexFromPos(o);const n=t.getValue();return r=S(r,n),function(e,t,o){const r=e.pipe(Object(R.childOf)(o),Object(R.ofMessageType)("complete_reply"),Object(v.a)(e=>e.content),Object(M.a)(),Object(v.a)(F(t)),Object(O.a)(15e3));return E.a.create(t=>{const n=r.subscribe(t);return e.next(o),n})}(e,t,A(n,r))}const I=(e,t)=>Object(R.createMessage)("inspect_request",{content:{code:e,cursor_pos:t,detail_level:0}});function T(e,t){const o=t.getCursor(),r=S(t.indexFromPos(o),t.getValue()),n=t.getValue();return function(e,t,o){const r=e.pipe(Object(R.childOf)(o),Object(R.ofMessageType)("inspect_reply"),Object(v.a)(e=>e.content),Object(M.a)(),Object(v.a)(e=>({dict:e.data})));return E.a.create(t=>{const n=r.subscribe(t);return e.next(o),n})}(e,0,I(n,r))}o(1015);var z=o(9),V=z.b`
  /* BASICS */

  .CodeMirror {
    /* Set height, width, borders, and global font properties here */
    font-family: monospace;
    height: 300px;
    color: black;
    direction: ltr;
  }

  /* PADDING */

  .CodeMirror-lines {
    padding: 4px 0; /* Vertical padding around content */
  }
  .CodeMirror pre {
    padding: 0 4px; /* Horizontal padding of content */
  }

  .CodeMirror-scrollbar-filler,
  .CodeMirror-gutter-filler {
    background-color: white; /* The little square between H and V scrollbars */
  }

  /* GUTTER */

  .CodeMirror-gutters {
    border-right: 1px solid #ddd;
    background-color: #f7f7f7;
    white-space: nowrap;
  }
  .CodeMirror-linenumbers {
  }
  .CodeMirror-linenumber {
    padding: 0 3px 0 5px;
    min-width: 20px;
    text-align: right;
    color: #999;
    white-space: nowrap;
  }

  .CodeMirror-guttermarker {
    color: black;
  }
  .CodeMirror-guttermarker-subtle {
    color: #999;
  }

  /* CURSOR */

  .CodeMirror-cursor {
    border-left: 1px solid black;
    border-right: none;
    width: 0;
  }
  /* Shown when moving in bi-directional text */
  .CodeMirror div.CodeMirror-secondarycursor {
    border-left: 1px solid silver;
  }
  .cm-fat-cursor .CodeMirror-cursor {
    width: auto;
    border: 0 !important;
    background: #7e7;
  }
  .cm-fat-cursor div.CodeMirror-cursors {
    z-index: 1;
  }
  .cm-fat-cursor-mark {
    background-color: rgba(20, 255, 20, 0.5);
    -webkit-animation: blink 1.06s steps(1) infinite;
    -moz-animation: blink 1.06s steps(1) infinite;
    animation: blink 1.06s steps(1) infinite;
  }
  .cm-animate-fat-cursor {
    width: auto;
    border: 0;
    -webkit-animation: blink 1.06s steps(1) infinite;
    -moz-animation: blink 1.06s steps(1) infinite;
    animation: blink 1.06s steps(1) infinite;
    background-color: #7e7;
  }
  @-moz-keyframes blink {
    0% {
    }
    50% {
      background-color: transparent;
    }
    100% {
    }
  }
  @-webkit-keyframes blink {
    0% {
    }
    50% {
      background-color: transparent;
    }
    100% {
    }
  }
  @keyframes blink {
    0% {
    }
    50% {
      background-color: transparent;
    }
    100% {
    }
  }

  /* Can style cursor different in overwrite (non-insert) mode */
  .CodeMirror-overwrite .CodeMirror-cursor {
  }

  .cm-tab {
    display: inline-block;
    text-decoration: inherit;
  }

  .CodeMirror-rulers {
    position: absolute;
    left: 0;
    right: 0;
    top: -50px;
    bottom: -20px;
    overflow: hidden;
  }
  .CodeMirror-ruler {
    border-left: 1px solid #ccc;
    top: 0;
    bottom: 0;
    position: absolute;
  }

  /* DEFAULT THEME */

  .cm-s-default .cm-header {
    color: blue;
  }
  .cm-s-default .cm-quote {
    color: #090;
  }
  .cm-negative {
    color: #d44;
  }
  .cm-positive {
    color: #292;
  }
  .cm-header,
  .cm-strong {
    font-weight: bold;
  }
  .cm-em {
    font-style: italic;
  }
  .cm-link {
    text-decoration: underline;
  }
  .cm-strikethrough {
    text-decoration: line-through;
  }

  .cm-s-default .cm-keyword {
    color: #708;
  }
  .cm-s-default .cm-atom {
    color: #219;
  }
  .cm-s-default .cm-number {
    color: #164;
  }
  .cm-s-default .cm-def {
    color: #00f;
  }
  .cm-s-default .cm-variable,
  .cm-s-default .cm-punctuation,
  .cm-s-default .cm-property,
  .cm-s-default .cm-operator {
  }
  .cm-s-default .cm-variable-2 {
    color: #05a;
  }
  .cm-s-default .cm-variable-3,
  .cm-s-default .cm-type {
    color: #085;
  }
  .cm-s-default .cm-comment {
    color: #a50;
  }
  .cm-s-default .cm-string {
    color: #a11;
  }
  .cm-s-default .cm-string-2 {
    color: #f50;
  }
  .cm-s-default .cm-meta {
    color: #555;
  }
  .cm-s-default .cm-qualifier {
    color: #555;
  }
  .cm-s-default .cm-builtin {
    color: #30a;
  }
  .cm-s-default .cm-bracket {
    color: #997;
  }
  .cm-s-default .cm-tag {
    color: #170;
  }
  .cm-s-default .cm-attribute {
    color: #00c;
  }
  .cm-s-default .cm-hr {
    color: #999;
  }
  .cm-s-default .cm-link {
    color: #00c;
  }

  .cm-s-default .cm-error {
    color: #f00;
  }
  .cm-invalidchar {
    color: #f00;
  }

  .CodeMirror-composing {
    border-bottom: 2px solid;
  }

  /* Default styles for common addons */

  div.CodeMirror span.CodeMirror-matchingbracket {
    color: #0b0;
  }
  div.CodeMirror span.CodeMirror-nonmatchingbracket {
    color: #a22;
  }
  .CodeMirror-matchingtag {
    background: rgba(255, 150, 0, 0.3);
  }
  .CodeMirror-activeline-background {
    background: #e8f2ff;
  }

  /* STOP */

  /* The rest of this file contains styles related to the mechanics of
   the editor. You probably shouldn't touch them. */

  .CodeMirror {
    position: relative;
    overflow: hidden;
    background: white;
  }

  .CodeMirror-scroll {
    overflow: scroll !important; /* Things will break if this is overridden */
    /* 30px is the magic margin used to hide the element's real scrollbars */
    /* See overflow: hidden in .CodeMirror */
    margin-bottom: -30px;
    margin-right: -30px;
    padding-bottom: 30px;
    height: 100%;
    outline: none; /* Prevent dragging from highlighting the element */
    position: relative;
  }
  .CodeMirror-sizer {
    position: relative;
    border-right: 30px solid transparent;
  }

  /* The fake, visible scrollbars. Used to force redraw during scrolling
   before actual scrolling happens, thus preventing shaking and
   flickering artifacts. */
  .CodeMirror-vscrollbar,
  .CodeMirror-hscrollbar,
  .CodeMirror-scrollbar-filler,
  .CodeMirror-gutter-filler {
    position: absolute;
    z-index: 6;
    display: none;
  }
  .CodeMirror-vscrollbar {
    right: 0;
    top: 0;
    overflow-x: hidden;
    overflow-y: scroll;
  }
  .CodeMirror-hscrollbar {
    bottom: 0;
    left: 0;
    overflow-y: hidden;
    overflow-x: scroll;
  }
  .CodeMirror-scrollbar-filler {
    right: 0;
    bottom: 0;
  }
  .CodeMirror-gutter-filler {
    left: 0;
    bottom: 0;
  }

  .CodeMirror-gutters {
    position: absolute;
    left: 0;
    top: 0;
    min-height: 100%;
    z-index: 3;
  }
  .CodeMirror-gutter {
    white-space: normal;
    height: 100%;
    display: inline-block;
    vertical-align: top;
    margin-bottom: -30px;
  }
  .CodeMirror-gutter-wrapper {
    position: absolute;
    z-index: 4;
    background: none !important;
    border: none !important;
  }
  .CodeMirror-gutter-background {
    position: absolute;
    top: 0;
    bottom: 0;
    z-index: 4;
  }
  .CodeMirror-gutter-elt {
    position: absolute;
    cursor: default;
    z-index: 4;
  }
  .CodeMirror-gutter-wrapper ::selection {
    background-color: transparent;
  }
  .CodeMirror-gutter-wrapper ::-moz-selection {
    background-color: transparent;
  }

  .CodeMirror-lines {
    cursor: text;
    min-height: 1px; /* prevents collapsing before first draw */
  }
  .CodeMirror pre {
    /* Reset some styles that the rest of the page might have set */
    -moz-border-radius: 0;
    -webkit-border-radius: 0;
    border-radius: 0;
    border-width: 0;
    background: transparent;
    font-family: inherit;
    font-size: inherit;
    margin: 0;
    white-space: pre;
    word-wrap: normal;
    line-height: inherit;
    color: inherit;
    z-index: 2;
    position: relative;
    overflow: visible;
    -webkit-tap-highlight-color: transparent;
    -webkit-font-variant-ligatures: contextual;
    font-variant-ligatures: contextual;
  }
  .CodeMirror-wrap pre {
    word-wrap: break-word;
    white-space: pre-wrap;
    word-break: normal;
  }

  .CodeMirror-linebackground {
    position: absolute;
    left: 0;
    right: 0;
    top: 0;
    bottom: 0;
    z-index: 0;
  }

  .CodeMirror-linewidget {
    position: relative;
    z-index: 2;
    padding: 0.1px; /* Force widget margins to stay inside of the container */
  }

  .CodeMirror-widget {
  }

  .CodeMirror-rtl pre {
    direction: rtl;
  }

  .CodeMirror-code {
    outline: none;
  }

  /* Force content-box sizing for the elements where we expect it */
  .CodeMirror-scroll,
  .CodeMirror-sizer,
  .CodeMirror-gutter,
  .CodeMirror-gutters,
  .CodeMirror-linenumber {
    -moz-box-sizing: content-box;
    box-sizing: content-box;
  }

  .CodeMirror-measure {
    position: absolute;
    width: 100%;
    height: 0;
    overflow: hidden;
    visibility: hidden;
  }

  .CodeMirror-cursor {
    position: absolute;
    pointer-events: none;
  }
  .CodeMirror-measure pre {
    position: static;
  }

  div.CodeMirror-cursors {
    visibility: hidden;
    position: relative;
    z-index: 3;
  }
  div.CodeMirror-dragcursors {
    visibility: visible;
  }

  .CodeMirror-focused div.CodeMirror-cursors {
    visibility: visible;
  }

  .CodeMirror-selected {
    background: #d9d9d9;
  }
  .CodeMirror-focused .CodeMirror-selected {
    background: #d7d4f0;
  }
  .CodeMirror-crosshair {
    cursor: crosshair;
  }
  .CodeMirror-line::selection,
  .CodeMirror-line > span::selection,
  .CodeMirror-line > span > span::selection {
    background: #d7d4f0;
  }
  .CodeMirror-line::-moz-selection,
  .CodeMirror-line > span::-moz-selection,
  .CodeMirror-line > span > span::-moz-selection {
    background: #d7d4f0;
  }

  .cm-searching {
    background-color: #ffa;
    background-color: rgba(255, 255, 0, 0.4);
  }

  /* Used to force a border model for a node */
  .cm-force-border {
    padding-right: 0.1px;
  }

  @media print {
    /* Hide the cursor when printing */
    .CodeMirror div.CodeMirror-cursors {
      visibility: hidden;
    }
  }

  /* See issue #2901 */
  .cm-tab-wrap-hack:after {
    content: "";
  }

  /* Help users use markselection to safely style text background */
  span.CodeMirror-selectedtext {
    background: none;
  }
`,P=z.b`
  .CodeMirror-hints {
    position: absolute;
    z-index: 10;
    overflow: hidden;
    list-style: none;

    margin: 0;
    padding: 2px;

    -webkit-box-shadow: 2px 3px 5px rgba(0, 0, 0, 0.2);
    -moz-box-shadow: 2px 3px 5px rgba(0, 0, 0, 0.2);
    box-shadow: 2px 3px 5px rgba(0, 0, 0, 0.2);
    border-radius: 3px;
    border: 1px solid silver;

    background: white;
    font-size: 90%;
    font-family: monospace;

    max-height: 20em;
    overflow-y: auto;
  }

  .CodeMirror-hint {
    margin: 0;
    padding: 0 4px;
    border-radius: 2px;
    white-space: pre;
    color: black;
    cursor: pointer;
  }

  li.CodeMirror-hint-active {
    background: #08f;
    color: white;
  }
`;const K=z.c.div`
  ${V}
  ${P}

    /* completions styles */
    .CodeMirror {
    height: 100%;
  }

  .CodeMirror-hint {
    padding-left: 0;
    border-bottom: none;
  }

  .completion-type {
    background: transparent;
    border: transparent 1px solid;
    width: 17px;
    height: 17px;
    margin: 0;
    padding: 0;
    display: inline-block;
    margin-right: 5px;
    top: 18px;
  }

  .completion-type:before {
    content: "?";
    bottom: 1px;
    left: 4px;
    position: relative;
  }
  /* color and content for each type of completion */
  .completion-type-keyword:before {
    content: "K";
  }
  .completion-type-keyword {
    background-color: darkred;
  }

  .completion-type-class:before {
    content: "C";
  }
  .completion-type-class {
    background-color: blueviolet;
  }

  .completion-type-module:before {
    content: "M";
  }
  .completion-type-module {
    background-color: chocolate;
  }

  .completion-type-statement:before {
    content: "S";
  }
  .completion-type-statement {
    background-color: forestgreen;
  }

  .completion-type-function:before {
    content: "ƒ";
  }
  .completion-type-function {
    background-color: yellowgreen;
  }

  .completion-type-instance:before {
    content: "I";
  }
  .completion-type-instance {
    background-color: teal;
  }

  .completion-type-null:before {
    content: "ø";
  }
  .completion-type-null {
    background-color: black;
  }

  /* end completion type color and content */

  /*
    Codemirror
 */

  .CodeMirror {
    font-family: "Source Code Pro";
    font-size: 14px;
    line-height: 20px;

    height: auto;

    background: none;
  }

  .CodeMirror-cursor {
    border-left-width: 1px;
    border-left-style: solid;
    border-left-color: var(--cm-color, black);
  }

  .CodeMirror-scroll {
    overflow-x: auto !important;
    overflow-y: hidden !important;
    width: 100%;
  }

  .CodeMirror-lines {
    padding: 0.4em;
  }

  .CodeMirror-linenumber {
    padding: 0 8px 0 4px;
  }

  .CodeMirror-gutters {
    border-top-left-radius: 2px;
    border-bottom-left-radius: 2px;
  }

  .cm-s-composition.CodeMirror {
    font-family: "Source Code Pro", monospace;
    letter-spacing: 0.3px;
    word-spacing: 0px;
    background: var(--cm-background, #fafafa);
    color: var(--cm-color, black);
  }
  .cm-s-composition .CodeMirror-lines {
    padding: 10px;
  }
  .cm-s-composition .CodeMirror-gutters {
    background-color: var(--cm-gutter-bg, white);
    padding-right: 10px;
    z-index: 3;
    border: none;
  }

  .cm-s-composition span.cm-comment {
    color: var(--cm-comment, #a86);
  }
  .cm-s-composition span.cm-keyword {
    line-height: 1em;
    font-weight: bold;
    color: var(--cm-keyword, blue);
  }
  .cm-s-composition span.cm-string {
    color: var(--cm-string, #a22);
  }
  .cm-s-composition span.cm-builtin {
    line-height: 1em;
    font-weight: bold;
    color: var(--cm-builtin, #077);
  }
  .cm-s-composition span.cm-special {
    line-height: 1em;
    font-weight: bold;
    color: var(--cm-special, #0aa);
  }
  .cm-s-composition span.cm-variable {
    color: var(--cm-variable, black);
  }
  .cm-s-composition span.cm-number,
  .cm-s-composition span.cm-atom {
    color: var(--cm-number, #3a3);
  }
  .cm-s-composition span.cm-meta {
    color: var(--cm-meta, #555);
  }
  .cm-s-composition span.cm-link {
    color: var(--cm-link, #3a3);
  }
  .cm-s-composition span.cm-operator {
    color: var(--cm-operator, black);
  }
  .cm-s-composition span.cm-def {
    color: var(--cm-def, black);
  }
  .cm-s-composition .CodeMirror-activeline-background {
    background: var(--cm-activeline-bg, #e8f2ff);
  }
  .cm-s-composition .CodeMirror-matchingbracket {
    border-bottom: 1px solid var(--cm-matchingbracket-outline, grey);
    color: var(--cm-matchingbracket-color, black) !important;
  }

  /* Overwrite some of the hint Styling */

  .CodeMirror-hints {
    -webkit-box-shadow: 2px 3px 5px rgba(0, 0, 0, 0.2);
    -moz-box-shadow: 2px 3px 5px rgba(0, 0, 0, 0.2);
    box-shadow: 2px 3px 5px rgba(0, 0, 0, 0.2);
    border-radius: 0px;
    border: none;
    padding: 0;

    background: var(--cm-hint-bg, white);
    font-size: 90%;
    font-family: "Source Code Pro", monospace;

    z-index: 9001;

    overflow-y: auto;
  }

  .CodeMirror-hint {
    border-radius: 0px;
    white-space: pre;
    cursor: pointer;
    color: var(--cm-hint-color, black);
  }

  li.CodeMirror-hint-active {
    background: var(--cm-hint-bg-active, #abd1ff);
    color: var(--cm-hint-color-active, black);
  }

  .initialTextAreaForCodeMirror {
    font-family: "Source Code Pro", "Monaco", monospace;
    font-size: 14px;
    line-height: 20px;

    height: inherit;

    background: none;

    border: none;
    overflow: hidden;

    -webkit-scrollbar: none;
    -webkit-box-shadow: none;
    -moz-box-shadow: none;
    box-shadow: none;
    width: 100%;
    resize: none;
    padding: 10px 0 5px 10px;
    letter-spacing: 0.3px;
    word-spacing: 0px;
  }

  .initialTextAreaForCodeMirror:focus {
    outline: none;
    border: none;
  }
`,q=z.c.button`
  float: right;
  display: inline-block;
  position: absolute;
  top: 0px;
  right: 0px;
  font-size: 11.5px;
`,B=z.c.div`
  padding: 20px 20px 50px 20px;
  margin: 30px 20px 50px 20px;
  box-shadow: 2px 2px 50px rgba(0, 0, 0, 0.2);
  white-space: pre-wrap;
  background-color: var(--theme-app-bg);
  z-index: 9999999;
`;function H(e){return e?e.replace(/\r\n|\r/g,"\n"):e}class U extends l.Component{constructor(e){super(e),this.hint=this.hint.bind(this),this.hint.async=!0,this.tips=this.tips.bind(this),this.deleteTip=this.deleteTip.bind(this),this.debounceNextCompletionRequest=!0,this.state={isFocused:!0,tipElement:null},this.defaultOptions=Object.assign({autoCloseBrackets:!0,lineNumbers:!1,matchBrackets:!0,theme:"composition",autofocus:!1,hintOptions:{hint:this.hint,completeSingle:!1,extraKeys:{Right:N}},extraKeys:{"Ctrl-Space":e=>(this.debounceNextCompletionRequest=!1,e.execCommand("autocomplete")),Tab:this.executeTab,"Shift-Tab":e=>e.execCommand("indentLess"),Up:this.goLineUpOrEmit,Down:this.goLineDownOrEmit,"Cmd-/":"toggleComment","Ctrl-/":"toggleComment","Cmd-.":this.tips,"Ctrl-.":this.tips},indentUnit:4,preserveScrollPosition:!1},e.options)}componentWillMount(){this.componentWillReceiveProps=Object(s.debounce)(this.componentWillReceiveProps,0)}componentDidMount(){const{completion:e,editorFocused:t,focusAbove:r,focusBelow:n}=this.props;o(1355),o(1356),o(1357),o(1358),o(1359),o(1176),o(1360),o(1361),o(1362),o(1363),o(1364),o(1365),o(1366),o(1367),o(1177),o(1369),o(1371),this.cm=o(853).fromTextArea(this.textarea,this.defaultOptions),this.cm.setValue(this.props.defaultValue||this.props.value||""),t&&this.cm.focus(),this.cm.on("topBoundary",r),this.cm.on("bottomBoundary",n),this.cm.on("focus",this.focusChanged.bind(this,!0)),this.cm.on("blur",this.focusChanged.bind(this,!1)),this.cm.on("change",this.codemirrorValueChanged.bind(this));const i=Object(d.a)(this.cm,"keyup",(e,t)=>({editor:e,ev:t}));this.keyupEventsSubscriber=i.pipe(Object(f.a)(e=>Object(p.a)(e))).subscribe(({editor:t,ev:o})=>{if(e&&!t.state.completionActive&&!w[(o.keyCode||o.which).toString()]){const e=t.getDoc().getCursor(),o=t.getTokenAt(e);"tag"!==o.type&&"variable"!==o.type&&" "!==o.string&&"<"!==o.string&&"/"!==o.string&&"."!==o.string||t.execCommand("autocomplete")}}),this.completionSubject=new u.b;const[s,l]=Object(b.a)(e=>!0===e.debounce)(this.completionSubject),a=Object(m.a)(l,s.pipe(Object(g.a)(150),Object(C.a)(l),Object(x.a)())).pipe(Object(f.a)(e=>{const{channels:t}=this.props;if(!t)throw new Error("Unexpectedly received a completion event when channels were unset");return D(t,e.editor).pipe(Object(v.a)(t=>()=>e.callback(t)),Object(C.a)(this.completionSubject),Object(k.a)(e=>(console.log("Code completion error: "+e.message),Object(h.b)())))}));this.completionEventsSubscriber=a.subscribe(e=>e())}componentDidUpdate(e){if(!this.cm)return;const{editorFocused:t,theme:o}=this.props,{cursorBlinkRate:r}=this.props.options;e.theme!==o&&this.cm.refresh(),e.editorFocused!==t&&(t?this.cm.focus():this.cm.getInputField().blur()),e.options.cursorBlinkRate!==r&&(this.cm.setOption("cursorBlinkRate",r),t&&(this.cm.getInputField().blur(),this.cm.focus())),e.options.mode!==this.props.options.mode&&this.cm.setOption("mode",this.props.options.mode)}componentWillReceiveProps(e){if(this.cm&&void 0!==e.value&&H(this.cm.getValue())!==H(e.value))if(this.props.options.preserveScrollPosition){var t=this.cm.getScrollInfo();this.cm.setValue(e.value),this.cm.scrollTo(t.left,t.top)}else this.cm.setValue(e.value);if("object"==typeof e.options)for(let t in e.options)e.options.hasOwnProperty(t)&&this.props.options[t]===e.options[t]&&this.cm.setOption(t,e.options[t])}componentWillUnmount(){this.cm&&this.cm.toTextArea(),this.keyupEventsSubscriber.unsubscribe(),this.completionEventsSubscriber.unsubscribe()}focusChanged(e){this.setState({isFocused:e}),this.props.onFocusChange&&this.props.onFocusChange(e)}hint(e,t){const{completion:o,channels:r}=this.props,n=this.debounceNextCompletionRequest;if(this.debounceNextCompletionRequest=!0,o&&r){const o={editor:e,callback:t,debounce:n};this.completionSubject.next(o)}}deleteTip(){this.setState({tipElement:null})}tips(e){const{tip:t,channels:o}=this.props;t&&T(o,e).subscribe(t=>{const o=t.dict;if(0===Object.keys(o).length)return;const r=document.getElementsByClassName("tip-holder")[0],n=c.a.createPortal(l.createElement(B,{className:"CodeMirror-hint"},l.createElement(y.b,{bundle:o,metadata:{expanded:!0}}),l.createElement(q,{onClick:this.deleteTip},"✕")),r);this.setState({tipElement:n}),e.addWidget({line:e.getCursor().line,ch:0},r,!0);const i=document.body;if(null!=r&&null!=i){const e=r.getBoundingClientRect();i.appendChild(r),r.style.top=e.top+"px"}})}goLineDownOrEmit(e){const t=e.getCursor(),r=e.lastLine(),n=e.getLine(r);if(t.line!==r||t.ch!==n.length||e.somethingSelected())e.execCommand("goLineDown");else{o(853).signal(e,"bottomBoundary")}}goLineUpOrEmit(e){const t=e.getCursor();if(0!==t.line||0!==t.ch||e.somethingSelected())e.execCommand("goLineUp");else{o(853).signal(e,"topBoundary")}}executeTab(e){e.somethingSelected()?e.execCommand("indentMore"):e.execCommand("insertSoftTab")}codemirrorValueChanged(e,t){this.props.onChange&&"setValue"!==t.origin&&this.props.onChange(e.getValue(),t)}render(){return l.createElement(K,{className:"CodeMirror cm-s-composition "},l.createElement("div",{className:"tip-holder"}),l.createElement("textarea",{ref:e=>{this.textarea=e},defaultValue:this.props.value,autoComplete:"off",className:"initialTextAreaForCodeMirror"}),this.state.tipElement)}}U.defaultProps={theme:"light",completion:!1,tip:!1,kernelStatus:"not connected",options:{},editorFocused:!1,channels:null};var L=U;t.a=Object(r.b)(function(e,t){const o=i.currentKernel(e),r=e.config.get("cursorBlinkRate",530);return Object.assign({},Object(s.omit)(t,["id","cellFocused","contentRef","options","channels","kernelStatus"]),{options:Object.assign({},t.options,{cursorBlinkRate:r}),channels:o?o.channels:null,kernelStatus:i.currentKernelStatus(e)||"not connected"})},(e,t)=>{const{cellFocused:o,id:r,contentRef:i}=t;return{onChange:t=>{e(n.updateCellSource({id:r,value:t,contentRef:i}))},onFocusChange(t){t&&(e(n.focusCellEditor({id:r,contentRef:i})),o||e(n.focusCell({id:r,contentRef:i})))}}})(L)},1791:function(e,t,o){"use strict";o.r(t),function(e){var r=o(66),n=o(1265);t.default=Object(r.hot)(e)(n.a)}.call(this,o(138)(e))}}]);