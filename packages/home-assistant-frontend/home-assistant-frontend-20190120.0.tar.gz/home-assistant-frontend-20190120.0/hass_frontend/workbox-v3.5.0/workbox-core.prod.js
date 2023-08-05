self.babelHelpers={asyncToGenerator:function(e){return function(){var r=e.apply(this,arguments);return new Promise(function(e,t){return function n(o,i){try{var c=r[o](i),l=c.value}catch(e){return void t(e)}if(!c.done)return Promise.resolve(l).then(function(e){n("next",e)},function(e){n("throw",e)});e(l)}("next")})}}},this.workbox=this.workbox||{},this.workbox.core=function(){"use strict";try{self.workbox.v["workbox:core:3.5.0"]=1}catch(e){}var e={debug:0,log:1,warn:2,error:3,silent:4};const r=/^((?!chrome|android).)*safari/i.test(navigator.userAgent);let t=(()=>e.warn)();const n=e=>t<=e,o=e=>t=e,i=()=>t,c=e.error,l=function(t,o,i){const l=0===t.indexOf("group")?c:e[t];if(!n(l))return;if(!i||"groupCollapsed"===t&&r)return void console[t](...o);const u=["%cworkbox",`background: ${i}; color: white; padding: 2px 0.5em; `+"border-radius: 0.5em;"];console[t](...u,...o)},u=()=>{n(c)&&console.groupEnd()},s={groupEnd:u,unprefixed:{groupEnd:u}},a={debug:"#7f8c8d",log:"#2ecc71",warn:"#f39c12",error:"#c0392b",groupCollapsed:"#3498db"};var f,d;Object.keys(a).forEach(e=>(e=e,d=a[e],s[e]=((...r)=>l(e,r,d)),void(s.unprefixed[e]=((...r)=>l(e,r)))));const h=(e,...r)=>{let t=e;return r.length>0&&(t+=` :: ${JSON.stringify(r)}`),t};class p extends Error{constructor(e,r){super(h(e,r)),this.name=e,this.details=r}}let b=(y=babelHelpers.asyncToGenerator(function*(){for(const e of g)yield e()}),function(){return y.apply(this,arguments)});var y;const g=new Set;class v{constructor(e,r,{onupgradeneeded:t,onversionchange:n=this.e}={}){this.r=e,this.t=r,this.n=t,this.e=n,this.o=null}open(){var e=this;return babelHelpers.asyncToGenerator(function*(){if(!e.o)return e.o=yield new Promise(function(r,t){let n=!1;setTimeout(function(){n=!0,t(new Error("The open request was blocked and timed out"))},e.OPEN_TIMEOUT);const o=indexedDB.open(e.r,e.t);o.onerror=function(e){return t(o.error)},o.onupgradeneeded=function(r){n?(o.transaction.abort(),r.target.result.close()):e.n&&e.n(r)},o.onsuccess=function(t){const o=t.target.result;n?o.close():(o.onversionchange=e.e,r(o))}}),e})()}get(e,...r){var t=this;return babelHelpers.asyncToGenerator(function*(){return yield t.i("get",e,"readonly",...r)})()}add(e,...r){var t=this;return babelHelpers.asyncToGenerator(function*(){return yield t.i("add",e,"readwrite",...r)})()}put(e,...r){var t=this;return babelHelpers.asyncToGenerator(function*(){return yield t.i("put",e,"readwrite",...r)})()}delete(e,...r){var t=this;return babelHelpers.asyncToGenerator(function*(){yield t.i("delete",e,"readwrite",...r)})()}deleteDatabase(){var e=this;return babelHelpers.asyncToGenerator(function*(){e.close(),e.o=null,yield new Promise(function(r,t){const n=indexedDB.deleteDatabase(e.r);n.onerror=function(e){return t(e.target.error)},n.onblocked=function(){return t(new Error("Deletion was blocked."))},n.onsuccess=function(){return r()}})})()}getAll(e,r,t){var n=this;return babelHelpers.asyncToGenerator(function*(){return"getAll"in IDBObjectStore.prototype?yield n.i("getAll",e,"readonly",r,t):yield n.getAllMatching(e,{query:r,count:t})})()}getAllMatching(e,r={}){var t=this;return babelHelpers.asyncToGenerator(function*(){return yield t.transaction([e],"readonly",function(t,n){const o=t[e],i=r.index?o.index(r.index):o,c=[],l=r.query||null,u=r.direction||"next";i.openCursor(l,u).onsuccess=function(e){const t=e.target.result;if(t){const{primaryKey:e,key:o,value:i}=t;c.push(r.includeKeys?{primaryKey:e,key:o,value:i}:i),r.count&&c.length>=r.count?n(c):t.continue()}else n(c)}})})()}transaction(e,r,t){var n=this;return babelHelpers.asyncToGenerator(function*(){return yield n.open(),yield new Promise(function(o,i){const c=n.o.transaction(e,r);c.onerror=function(e){return i(e.target.error)},c.onabort=function(e){return i(e.target.error)},c.oncomplete=function(){return o()};const l={};for(const r of e)l[r]=c.objectStore(r);t(l,function(e){return o(e)},function(){i(new Error("The transaction was manually aborted")),c.abort()})})})()}i(e,r,t,...n){var o=this;return babelHelpers.asyncToGenerator(function*(){yield o.open();return yield o.transaction([r],t,function(t,o){t[r][e](...n).onsuccess=function(e){o(e.target.result)}})})()}e(e){this.close()}close(){this.o&&this.o.close()}}v.prototype.OPEN_TIMEOUT=2e3;const w={prefix:"workbox",suffix:self.registration.scope,googleAnalytics:"googleAnalytics",precache:"precache",runtime:"runtime"},m=e=>[w.prefix,e,w.suffix].filter(e=>e.length>0).join("-"),E={updateDetails:e=>{Object.keys(w).forEach(r=>{void 0!==e[r]&&(w[r]=e[r])})},getGoogleAnalyticsName:e=>e||m(w.googleAnalytics),getPrecacheName:e=>e||m(w.precache),getRuntimeName:e=>e||m(w.runtime)};var L="cacheDidUpdate",x="cacheWillUpdate",H="cachedResponseWillBeUsed",k="fetchDidFail",q="requestWillFetch",D=(e,r)=>e.filter(e=>r in e);const N=e=>{const r=new URL(e,location);return r.origin===location.origin?r.pathname:r.href},O=(()=>{var e=babelHelpers.asyncToGenerator(function*(e,r,t,n=[]){if(!t)throw new p("cache-put-with-no-response",{url:N(r.url)});let o=yield P(r,t,n);if(!o)return;const i=yield caches.open(e),c=D(n,L);let l=c.length>0?yield R(e,r):null;try{yield i.put(r,o)}catch(e){throw"QuotaExceededError"===e.name&&(yield b()),e}for(let t of c)yield t[L].call(t,{cacheName:e,request:r,oldResponse:l,newResponse:o})});return function(r,t,n){return e.apply(this,arguments)}})(),R=(A=babelHelpers.asyncToGenerator(function*(e,r,t,n=[]){let o=yield(yield caches.open(e)).match(r,t);for(let i of n)H in i&&(o=yield i[H].call(i,{cacheName:e,request:r,matchOptions:t,cachedResponse:o}));return o}),function(e,r,t){return A.apply(this,arguments)});var A;const P=(W=babelHelpers.asyncToGenerator(function*(e,r,t){let n=r,o=!1;for(let r of t)if(x in r&&(o=!0,!(n=yield r[x].call(r,{request:e,response:n}))))break;return o||(n=n.ok?n:null),n||null}),function(e,r,t){return W.apply(this,arguments)});var W;const S={put:O,match:R},_={fetch:(()=>{var e=babelHelpers.asyncToGenerator(function*(e,r,t=[],n){if(n){const e=yield n;if(e)return e}"string"==typeof e&&(e=new Request(e));const o=D(t,k),i=o.length>0?e.clone():null;try{for(let r of t)q in r&&(e=yield r[q].call(r,{request:e.clone()}))}catch(e){throw new p("plugin-error-request-will-fetch",{thrownError:e})}const c=e.clone();try{return yield fetch(e,r)}catch(e){for(let r of o)yield r[k].call(r,{error:e,originalRequest:i.clone(),request:c.clone()});throw e}});return function(r,t){return e.apply(this,arguments)}})()};var j=Object.freeze({DBWrapper:v,WorkboxError:p,assert:null,cacheNames:E,cacheWrapper:S,fetchWrapper:_,getFriendlyURL:N,logger:s});var B=new class{constructor(){try{self.workbox.v=self.workbox.v||{}}catch(e){}}get cacheNames(){return{googleAnalytics:E.getGoogleAnalyticsName(),precache:E.getPrecacheName(),runtime:E.getRuntimeName()}}setCacheNameDetails(e){E.updateDetails(e)}get logLevel(){return i()}setLogLevel(r){if(r>e.silent||r<e.debug)throw new p("invalid-value",{paramName:"logLevel",validValueDescription:"Please use a value from LOG_LEVELS, i.e 'logLevel = workbox.core.LOG_LEVELS.debug'.",value:r});o(r)}};return Object.assign(B,{_private:j,LOG_LEVELS:e,registerQuotaErrorCallback:function(e){g.add(e)}})}();

//# sourceMappingURL=workbox-core.prod.js.map
