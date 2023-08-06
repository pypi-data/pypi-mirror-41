(window.webpackJsonp=window.webpackJsonp||[]).push([[5],{1292:function(e,t,n){"use strict";(function(e){var o=n(9),l=n(46),r=n(175),c=n(3),a=n(0),s=n(1189),i=n(1345),d=n.n(i),u=n(25),p=n(1356),m=n(1357),h=n(1358),f=n(1359),g=n(1360),b=n(1361),E=n(1801),v=n(1376),C=n(7);const y=c.List(),x=c.Set(),k=Object(C.c)(r.a).attrs(e=>({className:e.isSelected?"selected":""}))`
  /*
   * Show the cell-toolbar-mask if hovering on cell,
   * cell was the last clicked
   */
  &:hover ${E.a}, &.selected ${E.a} {
    display: block;
  }
`;k.displayName="Cell";const w=C.c.div`
  background-color: darkblue;
  color: ghostwhite;
  padding: 9px 16px;

  font-size: 12px;
  line-height: 20px;
`;w.displayName="CellBanner";const R=Object(u.b)((e,{id:t,contentRef:n})=>{return e=>{const l=o.r.model(e,{contentRef:n});if(!l||"notebook"!==l.type)throw new Error("Cell components should not be used with non-notebook models");const r=l.kernelRef,c=o.r.notebook.cellById(l,{id:t});if(!c)throw new Error("cell not found inside cell map");const a=c.cell_type,s=c.get("outputs",y),i="code"===a&&(c.getIn(["metadata","inputHidden"])||c.getIn(["metadata","hide_input"]))||!1,d="code"===a&&(0===s.size||c.getIn(["metadata","outputHidden"])),u="code"===a&&c.getIn(["metadata","outputExpanded"]),p=c.getIn(["metadata","tags"])||x,m=l.getIn(["cellPagers",t])||y;let h;if(r){const t=o.r.kernel(e,{kernelRef:r});t&&(h=t.channels)}return{cellFocused:l.cellFocused===t,cellStatus:l.transient.getIn(["cellMap",t,"status"]),cellType:a,channels:h,contentRef:n,editorFocused:l.editorFocused===t,executionCount:c.get("execution_count",null),outputExpanded:u,outputHidden:d,outputs:s,pager:m,source:c.get("source",""),sourceHidden:i,tags:p,theme:o.r.userTheme(e)}}},(e,{id:t,contentRef:n})=>{return e=>({focusAboveCell:()=>{e(o.a.focusPreviousCell({id:t,contentRef:n})),e(o.a.focusPreviousCellEditor({id:t,contentRef:n}))},focusBelowCell:()=>{e(o.a.focusNextCell({id:t,createCellIfUndefined:!0,contentRef:n})),e(o.a.focusNextCellEditor({id:t,contentRef:n}))},focusEditor:()=>e(o.a.focusCellEditor({id:t,contentRef:n})),selectCell:()=>e(o.a.focusCell({id:t,contentRef:n})),unfocusEditor:()=>e(o.a.focusCellEditor({id:void 0,contentRef:n})),updateOutputMetadata:(l,r)=>{e(o.a.updateOutputMetadata({id:t,contentRef:n,metadata:r,index:l}))}})})(class extends a.PureComponent{render(){const{cellFocused:e,cellStatus:t,cellType:n,editorFocused:o,focusAboveCell:c,focusBelowCell:s,focusEditor:i,id:d,tags:u,selectCell:p,unfocusEditor:m,contentRef:b,sourceHidden:C}=this.props,y="busy"===t,x="queued"===t;let R=null;switch(n){case"code":R=a.createElement(a.Fragment,null,a.createElement(r.d,{hidden:this.props.sourceHidden},a.createElement(r.h,{counter:this.props.executionCount,running:y,queued:x}),a.createElement(r.j,null,a.createElement(h.a,{id:d,contentRef:b,focusAbove:c,focusBelow:s}))),a.createElement(r.g,null,this.props.pager.map((e,t)=>a.createElement(l.d,{data:e.data,metadata:e.metadata},a.createElement(l.b.Json,null),a.createElement(l.b.JavaScript,null),a.createElement(l.b.HTML,null),a.createElement(l.b.Markdown,null),a.createElement(l.b.LaTeX,null),a.createElement(l.b.SVG,null),a.createElement(l.b.Image,null),a.createElement(l.b.Plain,null)))),a.createElement(r.f,{hidden:this.props.outputHidden,expanded:this.props.outputExpanded},this.props.outputs.map((e,t)=>a.createElement(l.c,{output:e,key:t},a.createElement(v.a,{output_type:"display_data",cellId:d,contentRef:b,index:t}),a.createElement(v.a,{output_type:"execute_result",cellId:d,contentRef:b,index:t}),a.createElement(l.a,null),a.createElement(l.e,null)))));break;case"markdown":R=a.createElement(g.a,{focusAbove:c,focusBelow:s,focusEditor:i,cellFocused:e,editorFocused:o,unfocusEditor:m,source:this.props.source},a.createElement(r.j,null,a.createElement(h.a,{id:d,contentRef:b,focusAbove:c,focusBelow:s})));break;case"raw":R=a.createElement(r.j,null,a.createElement(h.a,{id:d,contentRef:b,focusAbove:c,focusBelow:s}));break;default:R=a.createElement("pre",null,this.props.source)}return a.createElement(f.a,{focused:e,onClick:p},a.createElement(k,{isSelected:e},u.has("parameters")?a.createElement(w,null,"Papermill - Parametrized"):null,u.has("default parameters")?a.createElement(w,null,"Papermill - Default Parameters"):null,a.createElement(E.b,{type:n,sourceHidden:C,id:d,contentRef:b}),R))}}),O=C.c.div`
  padding-top: var(--nt-spacing-m, 10px);
  padding-left: var(--nt-spacing-m, 10px);
  padding-right: var(--nt-spacing-m, 10px);
`;class N extends a.PureComponent{constructor(e){super(e),this.keyDown=this.keyDown.bind(this)}componentDidMount(){document.addEventListener("keydown",this.keyDown)}componentWillUnmount(){document.removeEventListener("keydown",this.keyDown)}keyDown(t){if(13!==t.keyCode)return;const{executeFocusedCell:n,focusNextCell:o,focusNextCellEditor:l,contentRef:r}=this.props;let c=t.ctrlKey;"darwin"===e.platform&&(c=(t.metaKey||t.ctrlKey)&&!(t.metaKey&&t.ctrlKey)),(t.shiftKey||c)&&!(t.shiftKey&&c)&&(t.preventDefault(),n({contentRef:r}),t.shiftKey&&(o({id:void 0,createCellIfUndefined:!0,contentRef:r}),l({id:void 0,contentRef:r})))}render(){return a.createElement(a.Fragment,null,a.createElement(O,null,a.createElement(p.a,{id:this.props.cellOrder.get(0),above:!0,contentRef:this.props.contentRef}),this.props.cellOrder.map(e=>a.createElement("div",{className:"cell-container",key:`cell-container-${e}`},a.createElement(m.a,{moveCell:this.props.moveCell,id:e,focusCell:this.props.focusCell,contentRef:this.props.contentRef},a.createElement(R,{id:e,contentRef:this.props.contentRef})),a.createElement(p.a,{key:`creator-${e}`,id:e,above:!1,contentRef:this.props.contentRef})))),a.createElement(b.a,{contentRef:this.props.contentRef}),function(e){switch(e){case"dark":return a.createElement(r.b,null);case"light":default:return a.createElement(r.e,null)}}(this.props.theme))}}N.defaultProps={theme:"light"};const I=Object(s.DragDropContext)(d.a)(N);t.a=Object(u.b)((e,t)=>{const{contentRef:n}=t;if(!n)throw new Error("<Notebook /> has to have a contentRef");return e=>{const t=o.r.content(e,{contentRef:n}),l=o.r.model(e,{contentRef:n});if(!l||!t)throw new Error("<Notebook /> has to have content & model that are notebook types");const r=o.r.userTheme(e);if("notebook"!==l.type)return{cellOrder:c.List(),contentRef:n,theme:r};if("notebook"!==l.type)throw new Error("<Notebook /> has to have content & model that are notebook types");return{cellOrder:l.notebook.cellOrder,contentRef:n,theme:r}}},e=>({executeFocusedCell:t=>e(o.a.executeFocusedCell(t)),focusCell:t=>e(o.a.focusCell(t)),focusNextCell:t=>e(o.a.focusNextCell(t)),focusNextCellEditor:t=>e(o.a.focusNextCellEditor(t)),moveCell:t=>e(o.a.moveCell(t)),updateOutputMetadata:t=>e(o.a.updateOutputMetadata(t))}))(I)}).call(this,n(62))},1356:function(e,t,n){"use strict";var o=n(2),l=n(94),r=n(0),c=n(25),a=n(7);const s=a.c.div`
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
`,i=a.c.div`
  display: block;
  position: relative;
  overflow: visible;
  height: 0px;
`,d=a.c.div`
  position: relative;
  overflow: visible;
  top: -10px;
  height: 60px;
  text-align: center;

  &:hover ${s} {
    display: inline-block;
  }
`;class u extends r.PureComponent{constructor(){super(...arguments),this.createMarkdownCell=(()=>{this.props.createCell("markdown")}),this.createCodeCell=(()=>{this.props.createCell("code")})}render(){return r.createElement(i,null,r.createElement(d,null,r.createElement(s,null,r.createElement("button",{onClick:this.createMarkdownCell,title:"create text cell",className:"add-text-cell"},r.createElement("span",{className:"octicon"},r.createElement(l.g,null))),r.createElement("button",{onClick:this.createCodeCell,title:"create code cell",className:"add-code-cell"},r.createElement("span",{className:"octicon"},r.createElement(l.c,null))))))}}t.a=Object(c.b)(null,e=>({createCellAbove:t=>e(o.createCellAbove(t)),createCellAppend:t=>e(o.createCellAppend(t)),createCellBelow:t=>e(o.createCellBelow(t))}))(class extends r.PureComponent{constructor(){super(...arguments),this.createCell=(e=>{const{above:t,createCellBelow:n,createCellAppend:o,createCellAbove:l,id:r,contentRef:c}=this.props;void 0!==r&&"string"==typeof r?t?l({cellType:e,id:r,contentRef:c}):n({cellType:e,id:r,source:"",contentRef:c}):o({cellType:e,contentRef:c})})}render(){return r.createElement(u,{above:this.props.above,createCell:this.createCell})}})},1357:function(e,t,n){"use strict";var o=n(0),l=n(1189),r=n(7);const c=["data:image/png;base64,","iVBORw0KGgoAAAANSUhEUgAAADsAAAAzCAYAAAApdnDeAAAAAXNSR0IArs4c6QAA","AwNJREFUaAXtmlFL3EAUhe9MZptuoha3rLWgYC0W+lj/T3+26INvXbrI2oBdE9km","O9Nzxu1S0LI70AQScyFmDDfkfvdMZpNwlCCccwq7f21MaVM4FPtkU0o59RdoJBMx","WZINBg+DQWGKCAk+2kIKFh9JlSzLYVmOilEpR1Kh/iUbQFiNQTSbzWJrbYJximOJ","cSaulpVRoqh4K8JhjprIVJWqFlCpQNG51roYj8cLjJcGf5RMZWC1TYw1o2LxcEmy","0jeEo3ZFWVHIx0ji4eeKHFOx8l4sVVVZnBE6tWLHq7xO7FY86YpPeVjeo5y61tlR","JyhXEOQhF/lw6BGWixHvUWXVTpdgyUMu8q1h/ZJbqQhdiLsESx4FLvL9gcV6q3Cs","0liq2IHuBHjItYIV3rMvJnrYrkrdK9sr24EO9NO4AyI+i/CilOXbTi1xeXXFTyAS","GSOfzs42XmM+v5fJ5JvP29/fl8PDw43nhCbUpuzFxYXs7OxKmqZb1WQGkc/P80K+","T6dbnROaVJuyfPY+Pj7aup7h66HP/1Uu5O7u59bnhSTWpmxIEU3l9rBNdbrp6/TK","Nt3xpq7XK9tUp5u+Tm2/s/jYJdfX12LwBHVycrKRK89zmeJhYnZ7K3Fcz3e/2mDP","z7/waZEf8zaC+gSkKa3l4OBA3uztbXdOYFZtsKcfToNKSZNUPp6GnRN0AST3C1Ro","x9qS3yvbFqVC6+yVDe1YW/J7ZduiVGidvbKhHWtLfq9sW5QKrdMri9cxB6OFhQmO","TrDuBHjIRT5CEZZj0i7xOkYnWGeCPOQiHqC8lc/R60cLnNPuvjOkns7dk4t8/Jfv","s46mRlWqQiudxebVV3gAj7C9hXsmgZeztnfe/91YODEr3IoF/JY/sE2gbGaVLci3","hh0tRtWNvsm16JmNcOs6N9dW72LP7yOtWbEhjAUkZ+icoJ5HbE6+NSxMjKWe6cKb","GkUWgMwiFbXSlRpFkXelUlF4F70rVd7Bd4oZ/LL8xiDmtPV2Nwyf2zOlTfHERY7i","Haa1+w2+iFqx0aIgvgAAAABJRU5ErkJggg=="].join(""),a={beginDrag:e=>({id:e.id})},s=r.c.div.attrs({role:"presentation"})`
  position: absolute;
  z-index: 200;
  width: var(--prompt-width, 50px);
  height: 100%;
  cursor: move;
`,i=r.c.div.attrs(e=>({style:{opacity:e.isDragging?.25:1,borderTop:e.isOver&&e.hoverUpperHalf?"3px lightgray solid":"3px transparent solid",borderBottom:e.isOver&&!e.hoverUpperHalf?"3px lightgray solid":"3px transparent solid"}}))`
  position: relative;
  padding: 10px;
`;function d(e,t,n){const o=n.getBoundingClientRect(),l=(o.bottom-o.top)/2;return t.getClientOffset().y-o.top<l}const u={drop(e,t,n){if(t){const o=d(0,t,n.el);e.moveCell({id:t.getItem().id,destinationId:e.id,above:o,contentRef:e.contentRef})}},hover(e,t,n){t&&n.setState({hoverUpperHalf:d(0,t,n.el)})}};const p=Object(l.DragSource)("CELL",a,function(e,t){return{connectDragSource:e.dragSource(),isDragging:t.isDragging(),connectDragPreview:e.dragPreview()}}),m=Object(l.DropTarget)("CELL",u,function(e,t){return{connectDropTarget:e.dropTarget(),isOver:t.isOver()}});t.a=p(m(class extends o.Component{constructor(){super(...arguments),this.state={hoverUpperHalf:!0},this.selectCell=(()=>{const{focusCell:e,id:t,contentRef:n}=this.props;e({id:t,contentRef:n})})}componentDidMount(){const e=this.props.connectDragPreview,t=new window.Image;t.src=c,t.onload=(()=>{e(t)})}render(){return this.props.connectDropTarget(o.createElement("div",null,o.createElement(i,{isDragging:this.props.isDragging,hoverUpperHalf:this.state.hoverUpperHalf,isOver:this.props.isOver,ref:e=>{this.el=e}},this.props.connectDragSource(o.createElement("div",null,o.createElement(s,{onClick:this.selectCell}))),this.props.children)))}}))},1358:function(e,t,n){"use strict";var o=n(2),l=n(166),r=n(12),c=n(25);const a={name:"gfm",tokenTypeOverrides:{emoji:"emoji"}},s={name:"text/plain",tokenTypeOverrides:{emoji:"emoji"}};t.a=Object(c.b)((e,t)=>{const{id:n,contentRef:o,focusAbove:l,focusBelow:c}=t;return function(e){const t=r.model(e,{contentRef:o});if(!t||"notebook"!==t.type)throw new Error("Connected Editor components should not be used with non-notebook models");const i=r.notebook.cellById(t,{id:n});if(!i)throw new Error("cell not found inside cell map");t.cellFocused;const d=t.editorFocused===n,u=r.userTheme(e);let p=null,m="not connected",h=s,f=!1;switch(i.cell_type){case"markdown":f=!0,h=a;break;case"raw":f=!0,h=s;break;case"code":{const n=t.kernelRef,o=n?e.core.entities.kernels.byRef.get(n):null;p=o?o.channels:null,o&&(m=o.status||"not connected"),h=o&&o.info?o.info.codemirrorMode:r.notebook.codeMirrorMode(t)}}return{tip:!0,completion:!0,editorFocused:d,focusAbove:l,focusBelow:c,theme:u,value:i.source,channels:p,kernelStatus:m,cursorBlinkRate:e.config.get("cursorBlinkRate",530),mode:h,lineWrapping:f}}},(e,t)=>{const{id:n,contentRef:l}=t;return e=>({onChange:t=>{e(o.updateCellSource({id:n,value:t,contentRef:l}))},onFocusChange(t){t&&(e(o.focusCellEditor({id:n,contentRef:l})),e(o.focusCell({id:n,contentRef:l})))}})})(l.c)},1359:function(e,t,n){"use strict";n.d(t,"a",function(){return l});var o=n(0);class l extends o.Component{constructor(){super(...arguments),this.el=null}scrollIntoViewIfNeeded(e){const t=this.el&&this.el.parentElement&&this.el.parentElement.querySelector(":hover")===this.el;this.props.focused&&e!==this.props.focused&&!t&&(this.el&&"scrollIntoViewIfNeeded"in this.el?this.el.scrollIntoViewIfNeeded():this.el&&this.el.scrollIntoView())}componentDidUpdate(e){this.scrollIntoViewIfNeeded(e.focused)}componentDidMount(){this.scrollIntoViewIfNeeded()}render(){return o.createElement("div",{onClick:this.props.onClick,role:"presentation",ref:e=>{this.el=e}},this.props.children)}}},1360:function(e,t,n){"use strict";n.d(t,"a",function(){return s});var o=n(355),l=n(175),r=n(0),c=n.n(r);const a=()=>{};class s extends c.a.Component{constructor(e){super(e),this.state={view:!0},this.openEditor=this.openEditor.bind(this),this.editorKeyDown=this.editorKeyDown.bind(this),this.renderedKeyDown=this.renderedKeyDown.bind(this),this.closeEditor=this.closeEditor.bind(this)}componentDidMount(){this.updateFocus()}componentWillReceiveProps(e){this.setState({view:!e.editorFocused})}componentDidUpdate(){this.updateFocus()}updateFocus(){this.rendered&&this.state&&this.state.view&&this.props.cellFocused&&(this.rendered.focus(),this.props.editorFocused&&this.openEditor())}editorKeyDown(e){const t=e.shiftKey,n=e.ctrlKey;(t||n)&&"Enter"===e.key&&this.closeEditor()}closeEditor(){this.setState({view:!0}),this.props.unfocusEditor()}openEditor(){this.setState({view:!1}),this.props.focusEditor()}renderedKeyDown(e){const t=e.shiftKey,n=e.ctrlKey;if(!t&&!n||"Enter"!==e.key)switch(e.key){case"Enter":return this.openEditor(),void e.preventDefault();case"ArrowUp":this.props.focusAbove();break;case"ArrowDown":this.props.focusBelow()}else{if(this.state.view)return;this.closeEditor()}}render(){const e=this.props.source;return this.state&&this.state.view?c.a.createElement("div",{onDoubleClick:this.openEditor,onKeyDown:this.renderedKeyDown,ref:e=>{this.rendered=e},tabIndex:this.props.cellFocused?0:void 0,style:{outline:"none"}},c.a.createElement(l.f,null,c.a.createElement(o.a,{source:e||"*Empty markdown cell, double click me to add content.*"}))):c.a.createElement("div",{onKeyDown:this.editorKeyDown},c.a.createElement(l.d,null,c.a.createElement(l.i,null),this.props.children),c.a.createElement(l.f,{hidden:""===e},c.a.createElement(o.a,{source:e||"*Empty markdown cell, double click me to add content.*"})))}}s.defaultProps={cellFocused:!1,editorFocused:!1,focusAbove:a,focusBelow:a,focusEditor:a,unfocusEditor:a,source:""}},1361:function(e,t,n){"use strict";var o=n(12),l=n(1362),r=n.n(l),c=n(0),a=n.n(c),s=n(25),i=n(7);const d=i.c.div`
  float: left;
  display: block;
  padding-left: 10px;
`,u=i.c.div`
  float: right;
  padding-right: 10px;
  display: block;
`,p=i.c.div`
  position: fixed;
  bottom: 0;
  left: 0;
  width: 100%;
  font-size: 12px;
  line-height: 0.5em;
  background: var(--status-bar);
  z-index: 99;
`;t.a=Object(s.b)((e,t)=>{const{contentRef:n}=t;return e=>{const t=o.content(e,{contentRef:n});if(!t||"notebook"!==t.type)return{kernelStatus:"not connected",kernelSpecDisplayName:"no kernel",lastSaved:null};const l=t.model.kernelRef;let r=null;l&&(r=o.kernel(e,{kernelRef:l}));const c=t&&t.lastSaved?t.lastSaved:null,a=null!=r&&null!=r.status?r.status:"not connected";let s=" ";return"not connected"===a?s="no kernel":null!=r&&null!=r.kernelSpecName?s=r.kernelSpecName:void 0!==t&&"notebook"===t.type&&(s=o.notebook.displayName(t.model)||" "),{kernelSpecDisplayName:s,kernelStatus:a,lastSaved:c}}})(class extends a.a.Component{shouldComponentUpdate(e){return this.props.lastSaved!==e.lastSaved||this.props.kernelStatus!==e.kernelStatus}render(){const e=this.props.kernelSpecDisplayName||"Loading...";return a.a.createElement(p,null,a.a.createElement(u,null,this.props.lastSaved?a.a.createElement("p",null," Last saved ",r()(this.props.lastSaved)," "):a.a.createElement("p",null," Not saved yet ")),a.a.createElement(d,null,a.a.createElement("p",null,e," | ",this.props.kernelStatus)))}})},1376:function(e,t,n){"use strict";var o=n(0),l=n.n(o),r=n(25),c=n(9);const a=Object(r.b)((e,t)=>{const{contentRef:n,index:o,cellId:l}=t;return e=>{const t=e.core.entities.contents.byRef.getIn([n,"model","notebook","cellMap",l,"outputs",o],null);if(!t||"display_data"!==t.output_type&&"execute_result"!==t.output_type)return console.warn("connected transform media managed to get a non media bundle output"),{Media:()=>null};const r=c.r.transformsById(e),a=((e,t,n)=>{const o=e.data;return t.find(e=>o.hasOwnProperty(e)&&(n.hasOwnProperty(e)||n.get(e,!1)))})(t,c.r.displayOrder(e),r);return a?{Media:c.r.transform(e,{id:a}),mediaType:a,output:t}:{Media:()=>null,mediaType:a,output:t}}},(e,t)=>{const{cellId:n,contentRef:o,index:l}=t;return e=>({mediaActions:{onMetadataChange:t=>{e(c.a.updateOutputMetadata({id:n,contentRef:o,metadata:t,index:l}))}}})})(e=>{const{Media:t,mediaActions:n,mediaType:o,output:r}=e;return o&&r?l.a.createElement(t,Object.assign({},n,{data:r.data[o],metadata:r.metadata.get(o)})):null});t.a=a},1801:function(e,t,n){"use strict";var o=n(2),l=n(0),r=n(134),c=n(7);const a=c.c.div`
  z-index: 10000;
  display: inline-block;
`;a.displayName="DropdownDiv";class s extends l.PureComponent{constructor(e){super(e),this.state={menuHidden:!0}}render(){return l.createElement(a,null,l.Children.map(this.props.children,e=>{const t=e;return Object(r.areComponentsEqual)(t.type,d)?l.cloneElement(t,{onClick:()=>{this.setState({menuHidden:!this.state.menuHidden})}}):Object(r.areComponentsEqual)(t.type,p)?this.state.menuHidden?null:l.cloneElement(t,{onItemClick:()=>{this.setState({menuHidden:!0})}}):e}))}}const i=c.c.div`
  user-select: none;
  margin: 0px;
  padding: 0px;
`;i.displayName="DropdownTriggerDiv";class d extends l.PureComponent{render(){return l.createElement(i,{onClick:this.props.onClick},this.props.children)}}const u=c.c.div`
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
`;u.displayName="DropdownContentDiv";class p extends l.PureComponent{render(){return l.createElement(u,null,l.createElement("ul",null,l.Children.map(this.props.children,e=>{const t=e;return l.cloneElement(t,{onClick:e=>{t.props.onClick(e),this.props.onItemClick(e)}})})))}}p.defaultProps={onItemClick:()=>{}};var m=n(94),h=n(25);n.d(t,"a",function(){return g});const f=c.c.div`
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
`,g=c.c.div.attrs(e=>({style:{display:e.sourceHidden?"block":"none"}}))`
  z-index: 9999;
  position: absolute;
  top: 0px;
  right: 0px;
  height: 34px;

  /* Set the left padding to 50px to give users extra room to move their
              mouse to the toolbar without causing the cell to go out of focus and thus
              hide the toolbar before they get there. */
  padding: 0px 0px 0px 50px;
`;class b extends l.PureComponent{render(){const{type:e,executeCell:t,deleteCell:n,sourceHidden:o}=this.props;return l.createElement(g,{sourceHidden:o},l.createElement(f,null,"markdown"!==e&&l.createElement("button",{onClick:t,title:"execute cell",className:"executeButton"},l.createElement("span",{className:"octicon"},l.createElement(m.j,null))),l.createElement(s,null,l.createElement(d,null,l.createElement("button",{title:"show additional actions"},l.createElement("span",{className:"octicon toggle-menu"},l.createElement(m.b,null)))),"code"===e?l.createElement(p,null,l.createElement("li",{onClick:this.props.clearOutputs,className:"clearOutput",role:"option","aria-selected":"false",tabIndex:0},l.createElement("a",null,"Clear Cell Output")),l.createElement("li",{onClick:this.props.toggleCellInputVisibility,className:"inputVisibility",role:"option","aria-selected":"false",tabIndex:0},l.createElement("a",null,"Toggle Input Visibility")),l.createElement("li",{onClick:this.props.toggleCellOutputVisibility,className:"outputVisibility",role:"option","aria-selected":"false",tabIndex:0},l.createElement("a",null,"Toggle Output Visibility")),l.createElement("li",{onClick:this.props.toggleOutputExpansion,className:"outputExpanded",role:"option","aria-selected":"false",tabIndex:0},l.createElement("a",null,"Toggle Expanded Output")),l.createElement("li",{onClick:this.props.toggleParameterCell,role:"option","aria-selected":"false",tabIndex:0},l.createElement("a",null,"Toggle Parameter Cell")),l.createElement("li",{onClick:this.props.changeCellType,className:"changeType",role:"option","aria-selected":"false",tabIndex:0},l.createElement("a",null,"Convert to Markdown Cell"))):l.createElement(p,null,l.createElement("li",{onClick:this.props.changeCellType,className:"changeType",role:"option","aria-selected":"false",tabIndex:0},l.createElement("a",null,"Convert to Code Cell")))),l.createElement("span",{className:"spacer"}),l.createElement("button",{onClick:n,title:"delete cell",className:"deleteButton"},l.createElement("span",{className:"octicon"},l.createElement(m.i,null)))))}}b.defaultProps={type:"code"};t.b=Object(h.b)(null,(e,t)=>{const{contentRef:n,id:l,type:r}=t;return e=>({changeCellType:()=>e(o.changeCellType({contentRef:n,id:l,to:"markdown"===r?"code":"markdown"})),clearOutputs:()=>e(o.clearOutputs({id:l,contentRef:n})),deleteCell:()=>e(o.deleteCell({id:l,contentRef:n})),executeCell:()=>e(o.executeCell({id:l,contentRef:n})),toggleCellInputVisibility:()=>e(o.toggleCellInputVisibility({id:l,contentRef:n})),toggleCellOutputVisibility:()=>e(o.toggleCellOutputVisibility({id:l,contentRef:n})),toggleOutputExpansion:()=>e(o.toggleOutputExpansion({id:l,contentRef:n})),toggleParameterCell:()=>e(o.toggleParameterCell({id:l,contentRef:n}))})})(b)},1804:function(e,t,n){"use strict";n.r(t);var o=n(1292);t.default=o.a}}]);