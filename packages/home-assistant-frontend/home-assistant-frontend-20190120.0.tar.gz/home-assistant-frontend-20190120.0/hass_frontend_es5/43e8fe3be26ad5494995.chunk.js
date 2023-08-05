(window.webpackJsonp=window.webpackJsonp||[]).push([[35],{154:function(module,__webpack_exports__,__webpack_require__){"use strict";__webpack_require__.d(__webpack_exports__,"a",function(){return computeStateDomain});var _compute_domain__WEBPACK_IMPORTED_MODULE_0__=__webpack_require__(159);function computeStateDomain(stateObj){return Object(_compute_domain__WEBPACK_IMPORTED_MODULE_0__.a)(stateObj.entity_id)}},159:function(module,__webpack_exports__,__webpack_require__){"use strict";__webpack_require__.d(__webpack_exports__,"a",function(){return computeDomain});function computeDomain(entityId){return entityId.substr(0,entityId.indexOf("."))}},160:function(module,__webpack_exports__,__webpack_require__){"use strict";__webpack_require__(96);function _typeof(obj){if("function"===typeof Symbol&&"symbol"===typeof Symbol.iterator){_typeof=function(obj){return typeof obj}}else{_typeof=function(obj){return obj&&"function"===typeof Symbol&&obj.constructor===Symbol&&obj!==Symbol.prototype?"symbol":typeof obj}}return _typeof(obj)}function _classCallCheck(instance,Constructor){if(!(instance instanceof Constructor)){throw new TypeError("Cannot call a class as a function")}}function _defineProperties(target,props){for(var i=0,descriptor;i<props.length;i++){descriptor=props[i];descriptor.enumerable=descriptor.enumerable||!1;descriptor.configurable=!0;if("value"in descriptor)descriptor.writable=!0;Object.defineProperty(target,descriptor.key,descriptor)}}function _createClass(Constructor,protoProps,staticProps){if(protoProps)_defineProperties(Constructor.prototype,protoProps);if(staticProps)_defineProperties(Constructor,staticProps);return Constructor}function _possibleConstructorReturn(self,call){if(call&&("object"===_typeof(call)||"function"===typeof call)){return call}return _assertThisInitialized(self)}function _assertThisInitialized(self){if(void 0===self){throw new ReferenceError("this hasn't been initialised - super() hasn't been called")}return self}function _get(target,property,receiver){if("undefined"!==typeof Reflect&&Reflect.get){_get=Reflect.get}else{_get=function(target,property,receiver){var base=_superPropBase(target,property);if(!base)return;var desc=Object.getOwnPropertyDescriptor(base,property);if(desc.get){return desc.get.call(receiver)}return desc.value}}return _get(target,property,receiver||target)}function _superPropBase(object,property){while(!Object.prototype.hasOwnProperty.call(object,property)){object=_getPrototypeOf(object);if(null===object)break}return object}function _getPrototypeOf(o){_getPrototypeOf=Object.setPrototypeOf?Object.getPrototypeOf:function(o){return o.__proto__||Object.getPrototypeOf(o)};return _getPrototypeOf(o)}function _inherits(subClass,superClass){if("function"!==typeof superClass&&null!==superClass){throw new TypeError("Super expression must either be null or a function")}subClass.prototype=Object.create(superClass&&superClass.prototype,{constructor:{value:subClass,writable:!0,configurable:!0}});if(superClass)_setPrototypeOf(subClass,superClass)}function _setPrototypeOf(o,p){_setPrototypeOf=Object.setPrototypeOf||function(o,p){o.__proto__=p;return o};return _setPrototypeOf(o,p)}var IronIconClass=customElements.get("iron-icon"),loaded=!1,HaIcon=function(_IronIconClass){_inherits(HaIcon,_IronIconClass);function HaIcon(){_classCallCheck(this,HaIcon);return _possibleConstructorReturn(this,_getPrototypeOf(HaIcon).apply(this,arguments))}_createClass(HaIcon,[{key:"listen",value:function(){for(var _get2,_len=arguments.length,args=Array(_len),_key=0;_key<_len;_key++){args[_key]=arguments[_key]}(_get2=_get(_getPrototypeOf(HaIcon.prototype),"listen",this)).call.apply(_get2,[this].concat(args));if(!loaded&&"mdi"===this._iconsetName){loaded=!0;__webpack_require__.e(49).then(__webpack_require__.bind(null,213))}}}]);return HaIcon}(IronIconClass);customElements.define("ha-icon",HaIcon)},165:function(module,__webpack_exports__,__webpack_require__){"use strict";var _polymer_polymer_polymer_legacy_js__WEBPACK_IMPORTED_MODULE_0__=__webpack_require__(3),_polymer_polymer_lib_legacy_polymer_fn_js__WEBPACK_IMPORTED_MODULE_1__=__webpack_require__(4),_polymer_polymer_lib_utils_html_tag_js__WEBPACK_IMPORTED_MODULE_2__=__webpack_require__(1),_polymer_polymer_lib_utils_resolve_url_js__WEBPACK_IMPORTED_MODULE_3__=__webpack_require__(12);function _templateObject(){var data=_taggedTemplateLiteral(["\n    <style>\n      :host {\n        display: inline-block;\n        overflow: hidden;\n        position: relative;\n      }\n\n      #baseURIAnchor {\n        display: none;\n      }\n\n      #sizedImgDiv {\n        position: absolute;\n        top: 0px;\n        right: 0px;\n        bottom: 0px;\n        left: 0px;\n\n        display: none;\n      }\n\n      #img {\n        display: block;\n        width: var(--iron-image-width, auto);\n        height: var(--iron-image-height, auto);\n      }\n\n      :host([sizing]) #sizedImgDiv {\n        display: block;\n      }\n\n      :host([sizing]) #img {\n        display: none;\n      }\n\n      #placeholder {\n        position: absolute;\n        top: 0px;\n        right: 0px;\n        bottom: 0px;\n        left: 0px;\n\n        background-color: inherit;\n        opacity: 1;\n\n        @apply --iron-image-placeholder;\n      }\n\n      #placeholder.faded-out {\n        transition: opacity 0.5s linear;\n        opacity: 0;\n      }\n    </style>\n\n    <a id=\"baseURIAnchor\" href=\"#\"></a>\n    <div id=\"sizedImgDiv\" role=\"img\" hidden$=\"[[_computeImgDivHidden(sizing)]]\" aria-hidden$=\"[[_computeImgDivARIAHidden(alt)]]\" aria-label$=\"[[_computeImgDivARIALabel(alt, src)]]\"></div>\n    <img id=\"img\" alt$=\"[[alt]]\" hidden$=\"[[_computeImgHidden(sizing)]]\" crossorigin$=\"[[crossorigin]]\" on-load=\"_imgOnLoad\" on-error=\"_imgOnError\">\n    <div id=\"placeholder\" hidden$=\"[[_computePlaceholderHidden(preload, fade, loading, loaded)]]\" class$=\"[[_computePlaceholderClassName(preload, fade, loading, loaded)]]\"></div>\n"],["\n    <style>\n      :host {\n        display: inline-block;\n        overflow: hidden;\n        position: relative;\n      }\n\n      #baseURIAnchor {\n        display: none;\n      }\n\n      #sizedImgDiv {\n        position: absolute;\n        top: 0px;\n        right: 0px;\n        bottom: 0px;\n        left: 0px;\n\n        display: none;\n      }\n\n      #img {\n        display: block;\n        width: var(--iron-image-width, auto);\n        height: var(--iron-image-height, auto);\n      }\n\n      :host([sizing]) #sizedImgDiv {\n        display: block;\n      }\n\n      :host([sizing]) #img {\n        display: none;\n      }\n\n      #placeholder {\n        position: absolute;\n        top: 0px;\n        right: 0px;\n        bottom: 0px;\n        left: 0px;\n\n        background-color: inherit;\n        opacity: 1;\n\n        @apply --iron-image-placeholder;\n      }\n\n      #placeholder.faded-out {\n        transition: opacity 0.5s linear;\n        opacity: 0;\n      }\n    </style>\n\n    <a id=\"baseURIAnchor\" href=\"#\"></a>\n    <div id=\"sizedImgDiv\" role=\"img\" hidden\\$=\"[[_computeImgDivHidden(sizing)]]\" aria-hidden\\$=\"[[_computeImgDivARIAHidden(alt)]]\" aria-label\\$=\"[[_computeImgDivARIALabel(alt, src)]]\"></div>\n    <img id=\"img\" alt\\$=\"[[alt]]\" hidden\\$=\"[[_computeImgHidden(sizing)]]\" crossorigin\\$=\"[[crossorigin]]\" on-load=\"_imgOnLoad\" on-error=\"_imgOnError\">\n    <div id=\"placeholder\" hidden\\$=\"[[_computePlaceholderHidden(preload, fade, loading, loaded)]]\" class\\$=\"[[_computePlaceholderClassName(preload, fade, loading, loaded)]]\"></div>\n"]);_templateObject=function(){return data};return data}function _taggedTemplateLiteral(strings,raw){if(!raw){raw=strings.slice(0)}return Object.freeze(Object.defineProperties(strings,{raw:{value:Object.freeze(raw)}}))}/**
@license
Copyright (c) 2016 The Polymer Project Authors. All rights reserved.
This code may only be used under the BSD style license found at http://polymer.github.io/LICENSE.txt
The complete set of authors may be found at http://polymer.github.io/AUTHORS.txt
The complete set of contributors may be found at http://polymer.github.io/CONTRIBUTORS.txt
Code distributed by Google as part of the polymer project is also
subject to an additional IP rights grant found at http://polymer.github.io/PATENTS.txt
*/Object(_polymer_polymer_lib_legacy_polymer_fn_js__WEBPACK_IMPORTED_MODULE_1__.a)({_template:Object(_polymer_polymer_lib_utils_html_tag_js__WEBPACK_IMPORTED_MODULE_2__.a)(_templateObject()),is:"iron-image",properties:{src:{type:String,value:""},alt:{type:String,value:null},crossorigin:{type:String,value:null},preventLoad:{type:Boolean,value:!1},sizing:{type:String,value:null,reflectToAttribute:!0},position:{type:String,value:"center"},preload:{type:Boolean,value:!1},placeholder:{type:String,value:null,observer:"_placeholderChanged"},fade:{type:Boolean,value:!1},loaded:{notify:!0,readOnly:!0,type:Boolean,value:!1},loading:{notify:!0,readOnly:!0,type:Boolean,value:!1},error:{notify:!0,readOnly:!0,type:Boolean,value:!1},width:{observer:"_widthChanged",type:Number,value:null},height:{observer:"_heightChanged",type:Number,value:null}},observers:["_transformChanged(sizing, position)","_loadStateObserver(src, preventLoad)"],created:function(){this._resolvedSrc=""},_imgOnLoad:function(){if(this.$.img.src!==this._resolveSrc(this.src)){return}this._setLoading(!1);this._setLoaded(!0);this._setError(!1)},_imgOnError:function(){if(this.$.img.src!==this._resolveSrc(this.src)){return}this.$.img.removeAttribute("src");this.$.sizedImgDiv.style.backgroundImage="";this._setLoading(!1);this._setLoaded(!1);this._setError(!0)},_computePlaceholderHidden:function(){return!this.preload||!this.fade&&!this.loading&&this.loaded},_computePlaceholderClassName:function(){return this.preload&&this.fade&&!this.loading&&this.loaded?"faded-out":""},_computeImgDivHidden:function(){return!this.sizing},_computeImgDivARIAHidden:function(){return""===this.alt?"true":void 0},_computeImgDivARIALabel:function(){if(null!==this.alt){return this.alt}if(""===this.src){return""}var resolved=this._resolveSrc(this.src);return resolved.replace(/[?|#].*/g,"").split("/").pop()},_computeImgHidden:function(){return!!this.sizing},_widthChanged:function(){this.style.width=isNaN(this.width)?this.width:this.width+"px"},_heightChanged:function(){this.style.height=isNaN(this.height)?this.height:this.height+"px"},_loadStateObserver:function(src,preventLoad){var newResolvedSrc=this._resolveSrc(src);if(newResolvedSrc===this._resolvedSrc){return}this._resolvedSrc="";this.$.img.removeAttribute("src");this.$.sizedImgDiv.style.backgroundImage="";if(""===src||preventLoad){this._setLoading(!1);this._setLoaded(!1);this._setError(!1)}else{this._resolvedSrc=newResolvedSrc;this.$.img.src=this._resolvedSrc;this.$.sizedImgDiv.style.backgroundImage="url(\""+this._resolvedSrc+"\")";this._setLoading(!0);this._setLoaded(!1);this._setError(!1)}},_placeholderChanged:function(){this.$.placeholder.style.backgroundImage=this.placeholder?"url(\""+this.placeholder+"\")":""},_transformChanged:function(){var sizedImgDivStyle=this.$.sizedImgDiv.style,placeholderStyle=this.$.placeholder.style;sizedImgDivStyle.backgroundSize=placeholderStyle.backgroundSize=this.sizing;sizedImgDivStyle.backgroundPosition=placeholderStyle.backgroundPosition=this.sizing?this.position:"";sizedImgDivStyle.backgroundRepeat=placeholderStyle.backgroundRepeat=this.sizing?"no-repeat":""},_resolveSrc:function(testSrc){var resolved=Object(_polymer_polymer_lib_utils_resolve_url_js__WEBPACK_IMPORTED_MODULE_3__.c)(testSrc,this.$.baseURIAnchor.href);if("/"===resolved[0]){resolved=(location.origin||location.protocol+"//"+location.host)+resolved}return resolved}})},330:function(module,__webpack_exports__,__webpack_require__){"use strict";var _polymer_iron_image_iron_image__WEBPACK_IMPORTED_MODULE_0__=__webpack_require__(165),_polymer_polymer_lib_utils_html_tag__WEBPACK_IMPORTED_MODULE_1__=__webpack_require__(1),_polymer_polymer_polymer_element__WEBPACK_IMPORTED_MODULE_2__=__webpack_require__(11),_mixins_events_mixin__WEBPACK_IMPORTED_MODULE_3__=__webpack_require__(50);function _typeof(obj){if("function"===typeof Symbol&&"symbol"===typeof Symbol.iterator){_typeof=function(obj){return typeof obj}}else{_typeof=function(obj){return obj&&"function"===typeof Symbol&&obj.constructor===Symbol&&obj!==Symbol.prototype?"symbol":typeof obj}}return _typeof(obj)}function _templateObject(){var data=_taggedTemplateLiteral(["\n      <style include=\"iron-positioning\"></style>\n      <style>\n        .marker {\n          vertical-align: top;\n          position: relative;\n          display: block;\n          margin: 0 auto;\n          width: 2.5em;\n          text-align: center;\n          height: 2.5em;\n          line-height: 2.5em;\n          font-size: 1.5em;\n          border-radius: 50%;\n          border: 0.1em solid\n            var(--ha-marker-color, var(--default-primary-color));\n          color: rgb(76, 76, 76);\n          background-color: white;\n        }\n        iron-image {\n          border-radius: 50%;\n        }\n      </style>\n\n      <div class=\"marker\">\n        <template is=\"dom-if\" if=\"[[entityName]]\"\n          >[[entityName]]</template\n        >\n        <template is=\"dom-if\" if=\"[[entityPicture]]\">\n          <iron-image\n            sizing=\"cover\"\n            class=\"fit\"\n            src=\"[[entityPicture]]\"\n          ></iron-image>\n        </template>\n      </div>\n    "]);_templateObject=function(){return data};return data}function _taggedTemplateLiteral(strings,raw){if(!raw){raw=strings.slice(0)}return Object.freeze(Object.defineProperties(strings,{raw:{value:Object.freeze(raw)}}))}function _classCallCheck(instance,Constructor){if(!(instance instanceof Constructor)){throw new TypeError("Cannot call a class as a function")}}function _defineProperties(target,props){for(var i=0,descriptor;i<props.length;i++){descriptor=props[i];descriptor.enumerable=descriptor.enumerable||!1;descriptor.configurable=!0;if("value"in descriptor)descriptor.writable=!0;Object.defineProperty(target,descriptor.key,descriptor)}}function _createClass(Constructor,protoProps,staticProps){if(protoProps)_defineProperties(Constructor.prototype,protoProps);if(staticProps)_defineProperties(Constructor,staticProps);return Constructor}function _possibleConstructorReturn(self,call){if(call&&("object"===_typeof(call)||"function"===typeof call)){return call}return _assertThisInitialized(self)}function _assertThisInitialized(self){if(void 0===self){throw new ReferenceError("this hasn't been initialised - super() hasn't been called")}return self}function _get(target,property,receiver){if("undefined"!==typeof Reflect&&Reflect.get){_get=Reflect.get}else{_get=function(target,property,receiver){var base=_superPropBase(target,property);if(!base)return;var desc=Object.getOwnPropertyDescriptor(base,property);if(desc.get){return desc.get.call(receiver)}return desc.value}}return _get(target,property,receiver||target)}function _superPropBase(object,property){while(!Object.prototype.hasOwnProperty.call(object,property)){object=_getPrototypeOf(object);if(null===object)break}return object}function _getPrototypeOf(o){_getPrototypeOf=Object.setPrototypeOf?Object.getPrototypeOf:function(o){return o.__proto__||Object.getPrototypeOf(o)};return _getPrototypeOf(o)}function _inherits(subClass,superClass){if("function"!==typeof superClass&&null!==superClass){throw new TypeError("Super expression must either be null or a function")}subClass.prototype=Object.create(superClass&&superClass.prototype,{constructor:{value:subClass,writable:!0,configurable:!0}});if(superClass)_setPrototypeOf(subClass,superClass)}function _setPrototypeOf(o,p){_setPrototypeOf=Object.setPrototypeOf||function(o,p){o.__proto__=p;return o};return _setPrototypeOf(o,p)}var HaEntityMarker=function(_EventsMixin){_inherits(HaEntityMarker,_EventsMixin);function HaEntityMarker(){_classCallCheck(this,HaEntityMarker);return _possibleConstructorReturn(this,_getPrototypeOf(HaEntityMarker).apply(this,arguments))}_createClass(HaEntityMarker,[{key:"ready",value:function(){var _this=this;_get(_getPrototypeOf(HaEntityMarker.prototype),"ready",this).call(this);this.addEventListener("click",function(ev){return _this.badgeTap(ev)})}},{key:"badgeTap",value:function(ev){ev.stopPropagation();if(this.entityId){this.fire("hass-more-info",{entityId:this.entityId})}}}],[{key:"template",get:function(){return Object(_polymer_polymer_lib_utils_html_tag__WEBPACK_IMPORTED_MODULE_1__.a)(_templateObject())}},{key:"properties",get:function(){return{hass:{type:Object},entityId:{type:String,value:""},entityName:{type:String,value:null},entityPicture:{type:String,value:null}}}}]);return HaEntityMarker}(Object(_mixins_events_mixin__WEBPACK_IMPORTED_MODULE_3__.a)(_polymer_polymer_polymer_element__WEBPACK_IMPORTED_MODULE_2__.a));customElements.define("ha-entity-marker",HaEntityMarker)},331:function(module,__webpack_exports__,__webpack_require__){"use strict";__webpack_require__.d(__webpack_exports__,"a",function(){return setupLeafletMap});function asyncGeneratorStep(gen,resolve,reject,_next,_throw,key,arg){try{var info=gen[key](arg),value=info.value}catch(error){reject(error);return}if(info.done){resolve(value)}else{Promise.resolve(value).then(_next,_throw)}}function _asyncToGenerator(fn){return function(){var self=this,args=arguments;return new Promise(function(resolve,reject){var gen=fn.apply(self,args);function _next(value){asyncGeneratorStep(gen,resolve,reject,_next,_throw,"next",value)}function _throw(err){asyncGeneratorStep(gen,resolve,reject,_next,_throw,"throw",err)}_next(void 0)})}}var setupLeafletMap=function(){var _ref=_asyncToGenerator(regeneratorRuntime.mark(function _callee(mapElement){var Leaflet,map,style;return regeneratorRuntime.wrap(function(_context){while(1){switch(_context.prev=_context.next){case 0:_context.next=2;return __webpack_require__.e(109).then(__webpack_require__.t.bind(null,440,7));case 2:Leaflet=_context.sent.default;Leaflet.Icon.Default.imagePath="/static/images/leaflet";map=Leaflet.map(mapElement);style=document.createElement("link");style.setAttribute("href","/static/images/leaflet/leaflet.css");style.setAttribute("rel","stylesheet");mapElement.parentNode.appendChild(style);map.setView([51.505,-.09],13);Leaflet.tileLayer("https://{s}.basemaps.cartocdn.com/light_all/{z}/{x}/{y}".concat(Leaflet.Browser.retina?"@2x.png":".png"),{attribution:"&copy; <a href=\"https://www.openstreetmap.org/copyright\">OpenStreetMap</a>, &copy; <a href=\"https://carto.com/attributions\">CARTO</a>",subdomains:"abcd",minZoom:0,maxZoom:20}).addTo(map);return _context.abrupt("return",[map,Leaflet]);case 12:case"end":return _context.stop();}}},_callee,this)}));return function(){return _ref.apply(this,arguments)}}()},726:function(module,__webpack_exports__,__webpack_require__){"use strict";__webpack_require__.r(__webpack_exports__);var _polymer_app_layout_app_toolbar_app_toolbar__WEBPACK_IMPORTED_MODULE_0__=__webpack_require__(109),_polymer_polymer_lib_utils_html_tag__WEBPACK_IMPORTED_MODULE_1__=__webpack_require__(1),_polymer_polymer_polymer_element__WEBPACK_IMPORTED_MODULE_2__=__webpack_require__(11),_components_ha_menu_button__WEBPACK_IMPORTED_MODULE_3__=__webpack_require__(134),_components_ha_icon__WEBPACK_IMPORTED_MODULE_4__=__webpack_require__(160),_ha_entity_marker__WEBPACK_IMPORTED_MODULE_5__=__webpack_require__(330),_common_entity_compute_state_domain__WEBPACK_IMPORTED_MODULE_6__=__webpack_require__(154),_common_entity_compute_state_name__WEBPACK_IMPORTED_MODULE_7__=__webpack_require__(106),_mixins_localize_mixin__WEBPACK_IMPORTED_MODULE_8__=__webpack_require__(72),_common_dom_setup_leaflet_map__WEBPACK_IMPORTED_MODULE_9__=__webpack_require__(331);function _typeof(obj){if("function"===typeof Symbol&&"symbol"===typeof Symbol.iterator){_typeof=function(obj){return typeof obj}}else{_typeof=function(obj){return obj&&"function"===typeof Symbol&&obj.constructor===Symbol&&obj!==Symbol.prototype?"symbol":typeof obj}}return _typeof(obj)}function _templateObject(){var data=_taggedTemplateLiteral(["\n      <style include=\"ha-style\">\n        #map {\n          height: calc(100% - 64px);\n          width: 100%;\n          z-index: 0;\n        }\n      </style>\n\n      <app-toolbar>\n        <ha-menu-button\n          narrow=\"[[narrow]]\"\n          show-menu=\"[[showMenu]]\"\n        ></ha-menu-button>\n        <div main-title>[[localize('panel.map')]]</div>\n      </app-toolbar>\n\n      <div id=\"map\"></div>\n    "]);_templateObject=function(){return data};return data}function _taggedTemplateLiteral(strings,raw){if(!raw){raw=strings.slice(0)}return Object.freeze(Object.defineProperties(strings,{raw:{value:Object.freeze(raw)}}))}function _slicedToArray(arr,i){return _arrayWithHoles(arr)||_iterableToArrayLimit(arr,i)||_nonIterableRest()}function _nonIterableRest(){throw new TypeError("Invalid attempt to destructure non-iterable instance")}function _iterableToArrayLimit(arr,i){var _arr=[],_n=!0,_d=!1,_e=void 0;try{for(var _i=arr[Symbol.iterator](),_s;!(_n=(_s=_i.next()).done);_n=!0){_arr.push(_s.value);if(i&&_arr.length===i)break}}catch(err){_d=!0;_e=err}finally{try{if(!_n&&null!=_i["return"])_i["return"]()}finally{if(_d)throw _e}}return _arr}function _arrayWithHoles(arr){if(Array.isArray(arr))return arr}function asyncGeneratorStep(gen,resolve,reject,_next,_throw,key,arg){try{var info=gen[key](arg),value=info.value}catch(error){reject(error);return}if(info.done){resolve(value)}else{Promise.resolve(value).then(_next,_throw)}}function _asyncToGenerator(fn){return function(){var self=this,args=arguments;return new Promise(function(resolve,reject){var gen=fn.apply(self,args);function _next(value){asyncGeneratorStep(gen,resolve,reject,_next,_throw,"next",value)}function _throw(err){asyncGeneratorStep(gen,resolve,reject,_next,_throw,"throw",err)}_next(void 0)})}}function _classCallCheck(instance,Constructor){if(!(instance instanceof Constructor)){throw new TypeError("Cannot call a class as a function")}}function _defineProperties(target,props){for(var i=0,descriptor;i<props.length;i++){descriptor=props[i];descriptor.enumerable=descriptor.enumerable||!1;descriptor.configurable=!0;if("value"in descriptor)descriptor.writable=!0;Object.defineProperty(target,descriptor.key,descriptor)}}function _createClass(Constructor,protoProps,staticProps){if(protoProps)_defineProperties(Constructor.prototype,protoProps);if(staticProps)_defineProperties(Constructor,staticProps);return Constructor}function _possibleConstructorReturn(self,call){if(call&&("object"===_typeof(call)||"function"===typeof call)){return call}return _assertThisInitialized(self)}function _assertThisInitialized(self){if(void 0===self){throw new ReferenceError("this hasn't been initialised - super() hasn't been called")}return self}function _get(target,property,receiver){if("undefined"!==typeof Reflect&&Reflect.get){_get=Reflect.get}else{_get=function(target,property,receiver){var base=_superPropBase(target,property);if(!base)return;var desc=Object.getOwnPropertyDescriptor(base,property);if(desc.get){return desc.get.call(receiver)}return desc.value}}return _get(target,property,receiver||target)}function _superPropBase(object,property){while(!Object.prototype.hasOwnProperty.call(object,property)){object=_getPrototypeOf(object);if(null===object)break}return object}function _getPrototypeOf(o){_getPrototypeOf=Object.setPrototypeOf?Object.getPrototypeOf:function(o){return o.__proto__||Object.getPrototypeOf(o)};return _getPrototypeOf(o)}function _inherits(subClass,superClass){if("function"!==typeof superClass&&null!==superClass){throw new TypeError("Super expression must either be null or a function")}subClass.prototype=Object.create(superClass&&superClass.prototype,{constructor:{value:subClass,writable:!0,configurable:!0}});if(superClass)_setPrototypeOf(subClass,superClass)}function _setPrototypeOf(o,p){_setPrototypeOf=Object.setPrototypeOf||function(o,p){o.__proto__=p;return o};return _setPrototypeOf(o,p)}var HaPanelMap=function(_LocalizeMixin){_inherits(HaPanelMap,_LocalizeMixin);function HaPanelMap(){_classCallCheck(this,HaPanelMap);return _possibleConstructorReturn(this,_getPrototypeOf(HaPanelMap).apply(this,arguments))}_createClass(HaPanelMap,[{key:"connectedCallback",value:function(){_get(_getPrototypeOf(HaPanelMap.prototype),"connectedCallback",this).call(this);this.loadMap()}},{key:"loadMap",value:function(){var _loadMap=_asyncToGenerator(regeneratorRuntime.mark(function _callee(){var _ref,_ref2;return regeneratorRuntime.wrap(function(_context){while(1){switch(_context.prev=_context.next){case 0:_context.next=2;return Object(_common_dom_setup_leaflet_map__WEBPACK_IMPORTED_MODULE_9__.a)(this.$.map);case 2:_ref=_context.sent;_ref2=_slicedToArray(_ref,2);this._map=_ref2[0];this.Leaflet=_ref2[1];this.drawEntities(this.hass);this._map.invalidateSize();this.fitMap();case 9:case"end":return _context.stop();}}},_callee,this)}));return function(){return _loadMap.apply(this,arguments)}}()},{key:"disconnectedCallback",value:function(){if(this._map){this._map.remove()}}},{key:"fitMap",value:function(){var bounds;if(0===this._mapItems.length){this._map.setView(new this.Leaflet.LatLng(this.hass.config.latitude,this.hass.config.longitude),14)}else{bounds=new this.Leaflet.latLngBounds(this._mapItems.map(function(item){return item.getLatLng()}));this._map.fitBounds(bounds.pad(.5))}}},{key:"drawEntities",value:function(hass){var _this=this,map=this._map;if(!map)return;if(this._mapItems){this._mapItems.forEach(function(marker){marker.remove()})}var mapItems=this._mapItems=[];Object.keys(hass.states).forEach(function(entityId){var entity=hass.states[entityId],title=Object(_common_entity_compute_state_name__WEBPACK_IMPORTED_MODULE_7__.a)(entity);if(entity.attributes.hidden&&"zone"!==Object(_common_entity_compute_state_domain__WEBPACK_IMPORTED_MODULE_6__.a)(entity)||"home"===entity.state||!("latitude"in entity.attributes)||!("longitude"in entity.attributes)){return}var icon;if("zone"===Object(_common_entity_compute_state_domain__WEBPACK_IMPORTED_MODULE_6__.a)(entity)){if(entity.attributes.passive)return;var iconHTML="";if(entity.attributes.icon){var el=document.createElement("ha-icon");el.setAttribute("icon",entity.attributes.icon);iconHTML=el.outerHTML}else{iconHTML=title}icon=_this.Leaflet.divIcon({html:iconHTML,iconSize:[24,24],className:""});mapItems.push(_this.Leaflet.marker([entity.attributes.latitude,entity.attributes.longitude],{icon:icon,interactive:!1,title:title}).addTo(map));mapItems.push(_this.Leaflet.circle([entity.attributes.latitude,entity.attributes.longitude],{interactive:!1,color:"#FF9800",radius:entity.attributes.radius}).addTo(map));return}var entityPicture=entity.attributes.entity_picture||"",entityName=title.split(" ").map(function(part){return part.substr(0,1)}).join("");icon=_this.Leaflet.divIcon({html:"<ha-entity-marker entity-id='"+entity.entity_id+"' entity-name='"+entityName+"' entity-picture='"+entityPicture+"'></ha-entity-marker>",iconSize:[45,45],className:""});mapItems.push(_this.Leaflet.marker([entity.attributes.latitude,entity.attributes.longitude],{icon:icon,title:Object(_common_entity_compute_state_name__WEBPACK_IMPORTED_MODULE_7__.a)(entity)}).addTo(map));if(entity.attributes.gps_accuracy){mapItems.push(_this.Leaflet.circle([entity.attributes.latitude,entity.attributes.longitude],{interactive:!1,color:"#0288D1",radius:entity.attributes.gps_accuracy}).addTo(map))}})}}],[{key:"template",get:function(){return Object(_polymer_polymer_lib_utils_html_tag__WEBPACK_IMPORTED_MODULE_1__.a)(_templateObject())}},{key:"properties",get:function(){return{hass:{type:Object,observer:"drawEntities"},narrow:{type:Boolean},showMenu:{type:Boolean,value:!1}}}}]);return HaPanelMap}(Object(_mixins_localize_mixin__WEBPACK_IMPORTED_MODULE_8__.a)(_polymer_polymer_polymer_element__WEBPACK_IMPORTED_MODULE_2__.a));customElements.define("ha-panel-map",HaPanelMap)}}]);
//# sourceMappingURL=43e8fe3be26ad5494995.chunk.js.map