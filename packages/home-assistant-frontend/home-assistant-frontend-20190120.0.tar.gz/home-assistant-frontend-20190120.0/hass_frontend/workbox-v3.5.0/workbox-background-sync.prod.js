this.workbox=this.workbox||{},this.workbox.backgroundSync=function(e,t){"use strict";try{self.workbox.v["workbox:background-sync:3.5.0"]=1}catch(e){}const r=["method","referrer","referrerPolicy","mode","credentials","cache","redirect","integrity","keepalive"];class s{static fromRequest(e){return babelHelpers.asyncToGenerator(function*(){const t={headers:{}};"GET"!==e.method&&(t.body=yield e.clone().blob());for(const[r,s]of e.headers.entries())t.headers[r]=s;for(const s of r)void 0!==e[s]&&(t[s]=e[s]);return new s({url:e.url,requestInit:t})})()}constructor({url:e,requestInit:t,timestamp:r=Date.now()}){this.url=e,this.requestInit=t,this.e=r}get timestamp(){return this.e}toObject(){return{url:this.url,timestamp:this.timestamp,requestInit:this.requestInit}}toRequest(){return new Request(this.url,this.requestInit)}clone(){const e=Object.assign({},this.requestInit);return e.headers=Object.assign({},this.requestInit.headers),this.requestInit.body&&(e.body=this.requestInit.body.slice()),new s({url:this.url,timestamp:this.timestamp,requestInit:e})}}const i="workbox-background-sync",n="requests",u="queueName",c="workbox-background-sync",o=10080;class l{constructor(t){this.t=t,this.r=new e.DBWrapper(i,1,{onupgradeneeded:e=>e.target.result.createObjectStore(n,{autoIncrement:!0}).createIndex(u,u,{unique:!1})})}addEntry(e){var t=this;return babelHelpers.asyncToGenerator(function*(){yield t.r.add(n,{queueName:t.t.name,storableRequest:e.toObject()})})()}getAndRemoveOldestEntry(){var e=this;return babelHelpers.asyncToGenerator(function*(){const[t]=yield e.r.getAllMatching(n,{index:u,query:IDBKeyRange.only(e.t.name),count:1,includeKeys:!0});if(t)return yield e.r.delete(n,t.primaryKey),new s(t.value.storableRequest)})()}}const a=new Set;class h{constructor(e,{callbacks:r={},maxRetentionTime:s=o}={}){if(a.has(e))throw new t.WorkboxError("duplicate-queue-name",{name:e});a.add(e),this.s=e,this.i=r,this.n=s,this.u=new l(this),this.c()}get name(){return this.s}addRequest(e){var t=this;return babelHelpers.asyncToGenerator(function*(){const r=yield s.fromRequest(e.clone());yield t.o("requestWillEnqueue",r),yield t.u.addEntry(r),yield t.l()})()}replayRequests(){var e=this;return babelHelpers.asyncToGenerator(function*(){const r=Date.now(),s=[],i=[];let n;for(;n=yield e.u.getAndRemoveOldestEntry();){const t=n.clone(),u=60*e.n*1e3;if(r-n.timestamp>u)continue;yield e.o("requestWillReplay",n);const c={request:n.toRequest()};try{c.response=yield fetch(c.request.clone())}catch(e){c.error=e,i.push(t)}s.push(c)}if(yield e.o("queueDidReplay",s),i.length)throw yield Promise.all(i.map(function(t){return e.u.addEntry(t)})),new t.WorkboxError("queue-replay-failed",{name:e.s,count:i.length})})()}o(e,...t){var r=this;return babelHelpers.asyncToGenerator(function*(){"function"==typeof r.i[e]&&(yield r.i[e].apply(null,t))})()}c(){"sync"in registration?self.addEventListener("sync",e=>{e.tag===`${c}:${this.s}`&&e.waitUntil(this.replayRequests())}):this.replayRequests()}l(){var e=this;return babelHelpers.asyncToGenerator(function*(){if("sync"in registration)try{yield registration.sync.register(`${c}:${e.s}`)}catch(e){}})()}static get a(){return a}}return Object.freeze({Queue:h,Plugin:class{constructor(...e){this.t=new h(...e),this.fetchDidFail=this.fetchDidFail.bind(this)}fetchDidFail({request:e}){var t=this;return babelHelpers.asyncToGenerator(function*(){yield t.t.addRequest(e)})()}}})}(workbox.core._private,workbox.core._private);

//# sourceMappingURL=workbox-background-sync.prod.js.map
