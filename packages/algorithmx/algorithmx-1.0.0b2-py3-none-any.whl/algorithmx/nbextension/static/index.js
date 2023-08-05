define(["@jupyter-widgets/base","algorithmx"],function(e,t){return function(e){var t={};function n(s){if(t[s])return t[s].exports;var r=t[s]={i:s,l:!1,exports:{}};return e[s].call(r.exports,r,r.exports,n),r.l=!0,r.exports}return n.m=e,n.c=t,n.d=function(e,t,s){n.o(e,t)||Object.defineProperty(e,t,{enumerable:!0,get:s})},n.r=function(e){"undefined"!=typeof Symbol&&Symbol.toStringTag&&Object.defineProperty(e,Symbol.toStringTag,{value:"Module"}),Object.defineProperty(e,"__esModule",{value:!0})},n.t=function(e,t){if(1&t&&(e=n(e)),8&t)return e;if(4&t&&"object"==typeof e&&e&&e.__esModule)return e;var s=Object.create(null);if(n.r(s),Object.defineProperty(s,"default",{enumerable:!0,value:e}),2&t&&"string"!=typeof e)for(var r in e)n.d(s,r,function(t){return e[t]}.bind(null,r));return s},n.n=function(e){var t=e&&e.__esModule?function(){return e.default}:function(){return e};return n.d(t,"a",t),t},n.o=function(e,t){return Object.prototype.hasOwnProperty.call(e,t)},n.p="",n(n.s=1)}([function(e,t,n){"use strict";Object.defineProperty(t,"__esModule",{value:!0});const s=n(3);t.MODULE_VERSION=s.version,t.MODULE_NAME=s.name},function(e,t,n){"use strict";Object.defineProperty(t,"__esModule",{value:!0}),window.__webpack_public_path__=document.querySelector("body").getAttribute("data-base-url")+"nbextensions/algorithmx-jupyter",function(e){for(var n in e)t.hasOwnProperty(n)||(t[n]=e[n])}(n(2))},function(e,t,n){"use strict";function s(e){for(var n in e)t.hasOwnProperty(n)||(t[n]=e[n])}Object.defineProperty(t,"__esModule",{value:!0}),s(n(0)),s(n(4))},function(e){e.exports={name:"algorithmx-jupyter",version:"1.0.0-beta.1",description:"The AlgorithmX Jupyter Widget.",keywords:["jupyter","jupyterlab","jupyterlab-extension","widgets"],files:["lib/**/*.js","dist/*.js"],homepage:"https://github.com/algrx/algorithmx-python",bugs:{url:"https://github.com/algrx/algorithmx-python/issues"},license:"MIT",author:{name:"Alex Socha"},main:"lib/index.js",types:"./lib/index.d.ts",repository:{type:"git",url:"https://github.com/algrx/algorithmx-python"},scripts:{build:"npm run build:lib && npm run build:nbextension","build:labextension":"npm run clean:labextension && mkdirp algorithmx/labextension && cd algorithmx/labextension && npm pack ../..","build:lib":"tsc --project js","build:nbextension":"webpack -p","build:all":"npm run build:labextension && npm run build:nbextension",clean:"npm run clean:lib && npm run clean:nbextension","clean:lib":"rimraf lib","clean:labextension":"rimraf algorithmx/labextension","clean:nbextension":"rimraf algorithmx/nbextension/static/index.js",prepack:"npm run build:lib",test:"npm run test:firefox","test:chrome":"karma start --browsers=Chrome tests/karma.conf.js","test:debug":"karma start --browsers=Chrome --singleRun=false --debug=true tests/karma.conf.js","test:firefox":"karma start --browsers=Firefox tests/karma.conf.js","test:ie":"karma start --browsers=IE tests/karma.conf.js",watch:"npm-run-all -p watch:*","watch:lib":"tsc -w --project js","watch:nbextension":"webpack --watch"},dependencies:{"@jupyter-widgets/base":"^1.1.10",algorithmx:"latest"},devDependencies:{"@phosphor/application":"^1.6.0","@phosphor/widgets":"^1.6.0","@types/node":"^10.11.6","@types/webpack-env":"^1.13.6","fs-extra":"^7.0.0",mkdirp:"^0.5.1","npm-run-all":"^4.1.3",rimraf:"^2.6.2","source-map-loader":"^0.2.4","ts-loader":"^5.2.1",typescript:"~3.1.2",webpack:"^4.20.2","webpack-cli":"^3.1.2"},jupyterlab:{extension:"lib/plugin"}}},function(e,t,n){"use strict";var s=this&&this.__importStar||function(e){if(e&&e.__esModule)return e;var t={};if(null!=e)for(var n in e)Object.hasOwnProperty.call(e,n)&&(t[n]=e[n]);return t.default=e,t};Object.defineProperty(t,"__esModule",{value:!0});const r=n(5),i=n(0),o=s(n(6)),l=s(n(7));class a extends r.DOMWidgetModel{defaults(){return Object.assign({},super.defaults(),{_model_name:a.model_name,_model_module:a.model_module,_model_module_version:a.model_module_version,_view_name:a.view_name,_view_module:a.view_module,_view_module_version:a.view_module_version,_dispatch_events:[]})}}a.serializers=Object.assign({},r.DOMWidgetModel.serializers),a.model_name="CanvasModel",a.model_module=i.MODULE_NAME,a.model_module_version=i.MODULE_VERSION,a.view_name="CanvasModel",a.view_module=i.MODULE_NAME,a.view_module_version=i.MODULE_VERSION,t.CanvasModel=a;t.CanvasView=class extends r.DOMWidgetView{constructor(){super(...arguments),this.client=null,this.canvas=null,this.eventIndex=0,this.stopped=!1}playEvents(e){null!==this.client&&e.forEach(e=>{const t=JSON.parse(e);this.client.dispatch(t)})}playAllEvents(){const e=this.model.get("_dispatch_events");this.playEvents(e)}eventsChanged(){if(null===this.client)return;const e=this.model.get("_dispatch_events"),t=e.slice(this.eventIndex);this.eventIndex=e.length,this.playEvents(t)}resetCanvas(){if(null===this.canvas)return;const e=this.canvas.eventQ(null).duration(0);e.cancelall().startall(),e.remove(),e.add().size([400,250]).zoomkey(!0),setTimeout(()=>{e.svgattr("width","100%")},1)}removeCanvas(){this.resetCanvas();const e=this.el,t=e.querySelector("algorithmx-container");null!==t&&e.removeChild(t);const n=e.querySelector("algorithmx-buttons");null!==n&&e.removeChild(n)}remove(){this.removeCanvas(),super.remove()}clickRestart(){null!==this.canvas&&(this.resetCanvas(),this.playAllEvents(),this.stopped=!1)}clickStart(){null!==this.canvas&&(this.canvas.eventQ(null).startall(),this.stopped=!1)}clickStop(){null!==this.canvas&&(this.canvas.eventQ(null).stopall(),this.stopped=!0)}renderButtons(){const e=this.el,t=document.createElement("div"),n=o.createButton("pause",()=>{this.stopped?(o.setIcon(n,"pause"),this.clickStart()):(o.setIcon(n,"play"),this.clickStop())}),s=o.createButton("repeat",()=>{o.setIcon(n,"pause"),this.clickRestart()});t.appendChild(n),t.appendChild(s),e.appendChild(t)}render(){this.removeCanvas();const e=document.createElement("div");e.setAttribute("id","algorithmx-container"),this.client=l.client(e),this.client.subscribe(e=>{const t={source:"algorithmx",data:e},n=JSON.stringify(t);this.send(n)}),this.canvas=this.client.canvas(),this.resetCanvas(),this.el.appendChild(e),this.model.get("_show_buttons")&&this.renderButtons(),this.model.on("change:_dispatch_events",this.eventsChanged,this),this.eventsChanged()}}},function(t,n){t.exports=e},function(e,t,n){"use strict";Object.defineProperty(t,"__esModule",{value:!0});t.createButton=((e,n)=>{const s=document.createElement("div");t.createButton,s.onclick=n,s.style.width="28px",s.style.height="28px",s.style.backgroundColor="rgb(238, 238, 238)",s.style.display="inline-block",s.style.textAlign="center",s.style.marginRight="6px",s.style.cssFloat="left",s.onmouseover=(()=>{s.style.backgroundColor="rgb(220, 220, 220)",s.style.cursor="pointer"}),s.onmousedown=(()=>{s.style.backgroundColor="rgb(200, 200, 200)"}),s.onmouseup=(()=>{s.style.backgroundColor="rgb(220, 220, 220)"}),s.onmouseleave=(()=>{s.style.backgroundColor="rgb(238, 238, 238)",s.style.cursor=null});const r=document.createElement("i");return r.setAttribute("class",`fa-${e} fa`),r.style.fontSize="12px",r.style.color="rgb(50, 50, 50)",r.style.lineHeight="28px",s.appendChild(r),s}),t.setIcon=((e,t)=>{const n=e.querySelector("i");null!==n&&n.setAttribute("class",`fa-${t} fa`)})},function(e,n){e.exports=t}])});
//# sourceMappingURL=index.js.map