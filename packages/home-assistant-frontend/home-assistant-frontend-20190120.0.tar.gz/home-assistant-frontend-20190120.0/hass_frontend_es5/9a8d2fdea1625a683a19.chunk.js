(window.webpackJsonp=window.webpackJsonp||[]).push([[82],{156:function(module,__webpack_exports__,__webpack_require__){"use strict";var _polymer_polymer_polymer_legacy_js__WEBPACK_IMPORTED_MODULE_0__=__webpack_require__(3),_polymer_iron_flex_layout_iron_flex_layout_js__WEBPACK_IMPORTED_MODULE_1__=__webpack_require__(36),_polymer_paper_styles_default_theme_js__WEBPACK_IMPORTED_MODULE_2__=__webpack_require__(40),_polymer_paper_styles_typography_js__WEBPACK_IMPORTED_MODULE_3__=__webpack_require__(52),_polymer_polymer_lib_legacy_polymer_fn_js__WEBPACK_IMPORTED_MODULE_4__=__webpack_require__(4),_polymer_polymer_lib_utils_html_tag_js__WEBPACK_IMPORTED_MODULE_5__=__webpack_require__(1);function _templateObject(){var data=_taggedTemplateLiteral(["\n    <style>\n      :host {\n        overflow: hidden; /* needed for text-overflow: ellipsis to work on ff */\n        @apply --layout-vertical;\n        @apply --layout-center-justified;\n        @apply --layout-flex;\n      }\n\n      :host([two-line]) {\n        min-height: var(--paper-item-body-two-line-min-height, 72px);\n      }\n\n      :host([three-line]) {\n        min-height: var(--paper-item-body-three-line-min-height, 88px);\n      }\n\n      :host > ::slotted(*) {\n        overflow: hidden;\n        text-overflow: ellipsis;\n        white-space: nowrap;\n      }\n\n      :host > ::slotted([secondary]) {\n        @apply --paper-font-body1;\n\n        color: var(--paper-item-body-secondary-color, var(--secondary-text-color));\n\n        @apply --paper-item-body-secondary;\n      }\n    </style>\n\n    <slot></slot>\n"]);_templateObject=function(){return data};return data}function _taggedTemplateLiteral(strings,raw){if(!raw){raw=strings.slice(0)}return Object.freeze(Object.defineProperties(strings,{raw:{value:Object.freeze(raw)}}))}/**
@license
Copyright (c) 2015 The Polymer Project Authors. All rights reserved.
This code may only be used under the BSD style license found at
http://polymer.github.io/LICENSE.txt The complete set of authors may be found at
http://polymer.github.io/AUTHORS.txt The complete set of contributors may be
found at http://polymer.github.io/CONTRIBUTORS.txt Code distributed by Google as
part of the polymer project is also subject to an additional IP rights grant
found at http://polymer.github.io/PATENTS.txt
*/Object(_polymer_polymer_lib_legacy_polymer_fn_js__WEBPACK_IMPORTED_MODULE_4__.a)({_template:Object(_polymer_polymer_lib_utils_html_tag_js__WEBPACK_IMPORTED_MODULE_5__.a)(_templateObject()),is:"paper-item-body"})},163:function(module,__webpack_exports__,__webpack_require__){"use strict";var _polymer_polymer_polymer_legacy_js__WEBPACK_IMPORTED_MODULE_0__=__webpack_require__(3),_polymer_iron_flex_layout_iron_flex_layout_js__WEBPACK_IMPORTED_MODULE_1__=__webpack_require__(36),_polymer_paper_styles_typography_js__WEBPACK_IMPORTED_MODULE_2__=__webpack_require__(52),_paper_item_shared_styles_js__WEBPACK_IMPORTED_MODULE_3__=__webpack_require__(128),_polymer_polymer_lib_legacy_polymer_fn_js__WEBPACK_IMPORTED_MODULE_4__=__webpack_require__(4),_polymer_polymer_lib_utils_html_tag_js__WEBPACK_IMPORTED_MODULE_5__=__webpack_require__(1),_paper_item_behavior_js__WEBPACK_IMPORTED_MODULE_6__=__webpack_require__(107);function _templateObject(){var data=_taggedTemplateLiteral(["\n    <style include=\"paper-item-shared-styles\"></style>\n    <style>\n      :host {\n        @apply --layout-horizontal;\n        @apply --layout-center;\n        @apply --paper-font-subhead;\n\n        @apply --paper-item;\n        @apply --paper-icon-item;\n      }\n\n      .content-icon {\n        @apply --layout-horizontal;\n        @apply --layout-center;\n\n        width: var(--paper-item-icon-width, 56px);\n        @apply --paper-item-icon;\n      }\n    </style>\n\n    <div id=\"contentIcon\" class=\"content-icon\">\n      <slot name=\"item-icon\"></slot>\n    </div>\n    <slot></slot>\n"]);_templateObject=function(){return data};return data}function _taggedTemplateLiteral(strings,raw){if(!raw){raw=strings.slice(0)}return Object.freeze(Object.defineProperties(strings,{raw:{value:Object.freeze(raw)}}))}/**
@license
Copyright (c) 2015 The Polymer Project Authors. All rights reserved.
This code may only be used under the BSD style license found at
http://polymer.github.io/LICENSE.txt The complete set of authors may be found at
http://polymer.github.io/AUTHORS.txt The complete set of contributors may be
found at http://polymer.github.io/CONTRIBUTORS.txt Code distributed by Google as
part of the polymer project is also subject to an additional IP rights grant
found at http://polymer.github.io/PATENTS.txt
*/Object(_polymer_polymer_lib_legacy_polymer_fn_js__WEBPACK_IMPORTED_MODULE_4__.a)({_template:Object(_polymer_polymer_lib_utils_html_tag_js__WEBPACK_IMPORTED_MODULE_5__.a)(_templateObject()),is:"paper-icon-item",behaviors:[_paper_item_behavior_js__WEBPACK_IMPORTED_MODULE_6__.a]})},164:function(module,__webpack_exports__,__webpack_require__){"use strict";var _polymer_paper_icon_button_paper_icon_button__WEBPACK_IMPORTED_MODULE_0__=__webpack_require__(100),_polymer_paper_input_paper_input__WEBPACK_IMPORTED_MODULE_1__=__webpack_require__(79),_polymer_paper_item_paper_icon_item__WEBPACK_IMPORTED_MODULE_2__=__webpack_require__(163),_polymer_paper_item_paper_item_body__WEBPACK_IMPORTED_MODULE_3__=__webpack_require__(156),_polymer_polymer_lib_utils_html_tag__WEBPACK_IMPORTED_MODULE_4__=__webpack_require__(1),_polymer_polymer_polymer_element__WEBPACK_IMPORTED_MODULE_5__=__webpack_require__(11),_vaadin_vaadin_combo_box_vaadin_combo_box_light__WEBPACK_IMPORTED_MODULE_6__=__webpack_require__(183),_state_badge__WEBPACK_IMPORTED_MODULE_7__=__webpack_require__(162),_common_entity_compute_state_name__WEBPACK_IMPORTED_MODULE_8__=__webpack_require__(106),_mixins_localize_mixin__WEBPACK_IMPORTED_MODULE_9__=__webpack_require__(72),_mixins_events_mixin__WEBPACK_IMPORTED_MODULE_10__=__webpack_require__(50);function _typeof(obj){if("function"===typeof Symbol&&"symbol"===typeof Symbol.iterator){_typeof=function(obj){return typeof obj}}else{_typeof=function(obj){return obj&&"function"===typeof Symbol&&obj.constructor===Symbol&&obj!==Symbol.prototype?"symbol":typeof obj}}return _typeof(obj)}function _templateObject(){var data=_taggedTemplateLiteral(["\n      <style>\n        paper-input > paper-icon-button {\n          width: 24px;\n          height: 24px;\n          padding: 2px;\n          color: var(--secondary-text-color);\n        }\n        [hidden] {\n          display: none;\n        }\n      </style>\n      <vaadin-combo-box-light\n        items=\"[[_states]]\"\n        item-value-path=\"entity_id\"\n        item-label-path=\"entity_id\"\n        value=\"{{value}}\"\n        opened=\"{{opened}}\"\n        allow-custom-value=\"[[allowCustomEntity]]\"\n        on-change=\"_fireChanged\"\n      >\n        <paper-input\n          autofocus=\"[[autofocus]]\"\n          label=\"[[_computeLabel(label, localize)]]\"\n          class=\"input\"\n          autocapitalize=\"none\"\n          autocomplete=\"off\"\n          autocorrect=\"off\"\n          spellcheck=\"false\"\n          value=\"[[value]]\"\n          disabled=\"[[disabled]]\"\n        >\n          <paper-icon-button\n            slot=\"suffix\"\n            class=\"clear-button\"\n            icon=\"hass:close\"\n            no-ripple=\"\"\n            hidden$=\"[[!value]]\"\n            >Clear</paper-icon-button\n          >\n          <paper-icon-button\n            slot=\"suffix\"\n            class=\"toggle-button\"\n            icon=\"[[_computeToggleIcon(opened)]]\"\n            hidden=\"[[!_states.length]]\"\n            >Toggle</paper-icon-button\n          >\n        </paper-input>\n        <template>\n          <style>\n            paper-icon-item {\n              margin: -10px;\n              padding: 0;\n            }\n          </style>\n          <paper-icon-item>\n            <state-badge state-obj=\"[[item]]\" slot=\"item-icon\"></state-badge>\n            <paper-item-body two-line=\"\">\n              <div>[[_computeStateName(item)]]</div>\n              <div secondary=\"\">[[item.entity_id]]</div>\n            </paper-item-body>\n          </paper-icon-item>\n        </template>\n      </vaadin-combo-box-light>\n    "]);_templateObject=function(){return data};return data}function _taggedTemplateLiteral(strings,raw){if(!raw){raw=strings.slice(0)}return Object.freeze(Object.defineProperties(strings,{raw:{value:Object.freeze(raw)}}))}function _classCallCheck(instance,Constructor){if(!(instance instanceof Constructor)){throw new TypeError("Cannot call a class as a function")}}function _defineProperties(target,props){for(var i=0,descriptor;i<props.length;i++){descriptor=props[i];descriptor.enumerable=descriptor.enumerable||!1;descriptor.configurable=!0;if("value"in descriptor)descriptor.writable=!0;Object.defineProperty(target,descriptor.key,descriptor)}}function _createClass(Constructor,protoProps,staticProps){if(protoProps)_defineProperties(Constructor.prototype,protoProps);if(staticProps)_defineProperties(Constructor,staticProps);return Constructor}function _possibleConstructorReturn(self,call){if(call&&("object"===_typeof(call)||"function"===typeof call)){return call}return _assertThisInitialized(self)}function _assertThisInitialized(self){if(void 0===self){throw new ReferenceError("this hasn't been initialised - super() hasn't been called")}return self}function _getPrototypeOf(o){_getPrototypeOf=Object.setPrototypeOf?Object.getPrototypeOf:function(o){return o.__proto__||Object.getPrototypeOf(o)};return _getPrototypeOf(o)}function _inherits(subClass,superClass){if("function"!==typeof superClass&&null!==superClass){throw new TypeError("Super expression must either be null or a function")}subClass.prototype=Object.create(superClass&&superClass.prototype,{constructor:{value:subClass,writable:!0,configurable:!0}});if(superClass)_setPrototypeOf(subClass,superClass)}function _setPrototypeOf(o,p){_setPrototypeOf=Object.setPrototypeOf||function(o,p){o.__proto__=p;return o};return _setPrototypeOf(o,p)}var HaEntityPicker=function(_EventsMixin){_inherits(HaEntityPicker,_EventsMixin);function HaEntityPicker(){_classCallCheck(this,HaEntityPicker);return _possibleConstructorReturn(this,_getPrototypeOf(HaEntityPicker).apply(this,arguments))}_createClass(HaEntityPicker,[{key:"_computeLabel",value:function(label,localize){return label===void 0?localize("ui.components.entity.entity-picker.entity"):label}},{key:"_computeStates",value:function(hass,domainFilter,entityFilter){if(!hass)return[];var entityIds=Object.keys(hass.states);if(domainFilter){entityIds=entityIds.filter(function(eid){return eid.substr(0,eid.indexOf("."))===domainFilter})}var entities=entityIds.sort().map(function(key){return hass.states[key]});if(entityFilter){entities=entities.filter(entityFilter)}return entities}},{key:"_computeStateName",value:function(state){return Object(_common_entity_compute_state_name__WEBPACK_IMPORTED_MODULE_8__.a)(state)}},{key:"_openedChanged",value:function(newVal){if(!newVal){this._hass=this.hass}}},{key:"_hassChanged",value:function(newVal){if(!this.opened){this._hass=newVal}}},{key:"_computeToggleIcon",value:function(opened){return opened?"hass:menu-up":"hass:menu-down"}},{key:"_fireChanged",value:function(ev){ev.stopPropagation();this.fire("change")}}],[{key:"template",get:function(){return Object(_polymer_polymer_lib_utils_html_tag__WEBPACK_IMPORTED_MODULE_4__.a)(_templateObject())}},{key:"properties",get:function(){return{allowCustomEntity:{type:Boolean,value:!1},hass:{type:Object,observer:"_hassChanged"},_hass:Object,_states:{type:Array,computed:"_computeStates(_hass, domainFilter, entityFilter)"},autofocus:Boolean,label:{type:String},value:{type:String,notify:!0},opened:{type:Boolean,value:!1,observer:"_openedChanged"},domainFilter:{type:String,value:null},entityFilter:{type:Function,value:null},disabled:Boolean}}}]);return HaEntityPicker}(Object(_mixins_events_mixin__WEBPACK_IMPORTED_MODULE_10__.a)(Object(_mixins_localize_mixin__WEBPACK_IMPORTED_MODULE_9__.a)(_polymer_polymer_polymer_element__WEBPACK_IMPORTED_MODULE_5__.a)));customElements.define("ha-entity-picker",HaEntityPicker)},168:function(module,__webpack_exports__,__webpack_require__){"use strict";var index_es=__webpack_require__(200);__webpack_require__.d(__webpack_exports__,"a",function(){return struct});var struct=Object(index_es.a)({types:{"entity-id":function(value){if("string"!==typeof value){return"entity id should be a string"}if(!value.includes(".")){return"entity id should be in the format 'domain.entity'"}return!0},icon:function(value){if("string"!==typeof value){return"icon should be a string"}if(!value.includes(":")){return"icon should be in the format 'mdi:icon'"}return!0}}})},171:function(module,__webpack_exports__,__webpack_require__){"use strict";__webpack_require__.d(__webpack_exports__,"a",function(){return configElementStyle});var lit_element__WEBPACK_IMPORTED_MODULE_0__=__webpack_require__(41);function _templateObject(){var data=_taggedTemplateLiteral(["\n  <style>\n    paper-toggle-button {\n      padding-top: 16px;\n    }\n    .side-by-side {\n      display: flex;\n    }\n    .side-by-side > * {\n      flex: 1;\n      padding-right: 4px;\n    }\n  </style>\n"]);_templateObject=function(){return data};return data}function _taggedTemplateLiteral(strings,raw){if(!raw){raw=strings.slice(0)}return Object.freeze(Object.defineProperties(strings,{raw:{value:Object.freeze(raw)}}))}var configElementStyle=Object(lit_element__WEBPACK_IMPORTED_MODULE_0__.c)(_templateObject())},207:function(module,__webpack_exports__,__webpack_require__){"use strict";var lit_element__WEBPACK_IMPORTED_MODULE_0__=__webpack_require__(41),_polymer_paper_button_paper_button__WEBPACK_IMPORTED_MODULE_1__=__webpack_require__(73),_common_dom_fire_event__WEBPACK_IMPORTED_MODULE_2__=__webpack_require__(66),_mixins_lit_localize_mixin__WEBPACK_IMPORTED_MODULE_3__=__webpack_require__(155);function _typeof(obj){if("function"===typeof Symbol&&"symbol"===typeof Symbol.iterator){_typeof=function(obj){return typeof obj}}else{_typeof=function(obj){return obj&&"function"===typeof Symbol&&obj.constructor===Symbol&&obj!==Symbol.prototype?"symbol":typeof obj}}return _typeof(obj)}function _templateObject3(){var data=_taggedTemplateLiteral(["\n      <style>\n        paper-dropdown-menu {\n          width: 100%;\n        }\n      </style>\n    "]);_templateObject3=function(){return data};return data}function _templateObject2(){var data=_taggedTemplateLiteral(["\n                <paper-item theme=\"","\">","</paper-item>\n              "]);_templateObject2=function(){return data};return data}function _templateObject(){var data=_taggedTemplateLiteral(["\n      ","\n      <paper-dropdown-menu\n        label=\"Theme\"\n        dynamic-align\n        @value-changed=\"","\"\n      >\n        <paper-listbox\n          slot=\"dropdown-content\"\n          .selected=\"","\"\n          attr-for-selected=\"theme\"\n        >\n          ","\n        </paper-listbox>\n      </paper-dropdown-menu>\n    "]);_templateObject=function(){return data};return data}function _taggedTemplateLiteral(strings,raw){if(!raw){raw=strings.slice(0)}return Object.freeze(Object.defineProperties(strings,{raw:{value:Object.freeze(raw)}}))}function _classCallCheck(instance,Constructor){if(!(instance instanceof Constructor)){throw new TypeError("Cannot call a class as a function")}}function _defineProperties(target,props){for(var i=0,descriptor;i<props.length;i++){descriptor=props[i];descriptor.enumerable=descriptor.enumerable||!1;descriptor.configurable=!0;if("value"in descriptor)descriptor.writable=!0;Object.defineProperty(target,descriptor.key,descriptor)}}function _createClass(Constructor,protoProps,staticProps){if(protoProps)_defineProperties(Constructor.prototype,protoProps);if(staticProps)_defineProperties(Constructor,staticProps);return Constructor}function _possibleConstructorReturn(self,call){if(call&&("object"===_typeof(call)||"function"===typeof call)){return call}return _assertThisInitialized(self)}function _assertThisInitialized(self){if(void 0===self){throw new ReferenceError("this hasn't been initialised - super() hasn't been called")}return self}function _getPrototypeOf(o){_getPrototypeOf=Object.setPrototypeOf?Object.getPrototypeOf:function(o){return o.__proto__||Object.getPrototypeOf(o)};return _getPrototypeOf(o)}function _inherits(subClass,superClass){if("function"!==typeof superClass&&null!==superClass){throw new TypeError("Super expression must either be null or a function")}subClass.prototype=Object.create(superClass&&superClass.prototype,{constructor:{value:subClass,writable:!0,configurable:!0}});if(superClass)_setPrototypeOf(subClass,superClass)}function _setPrototypeOf(o,p){_setPrototypeOf=Object.setPrototypeOf||function(o,p){o.__proto__=p;return o};return _setPrototypeOf(o,p)}var HuiThemeSelectionEditor=function(_hassLocalizeLitMixin){_inherits(HuiThemeSelectionEditor,_hassLocalizeLitMixin);function HuiThemeSelectionEditor(){_classCallCheck(this,HuiThemeSelectionEditor);return _possibleConstructorReturn(this,_getPrototypeOf(HuiThemeSelectionEditor).apply(this,arguments))}_createClass(HuiThemeSelectionEditor,[{key:"render",value:function(){var themes=["Backend-selected","default"].concat(Object.keys(this.hass.themes.themes).sort());return Object(lit_element__WEBPACK_IMPORTED_MODULE_0__.c)(_templateObject(),this.renderStyle(),this._changed,this.value,themes.map(function(theme){return Object(lit_element__WEBPACK_IMPORTED_MODULE_0__.c)(_templateObject2(),theme,theme)}))}},{key:"renderStyle",value:function(){return Object(lit_element__WEBPACK_IMPORTED_MODULE_0__.c)(_templateObject3())}},{key:"_changed",value:function(ev){if(!this.hass||""===ev.target.value){return}this.value=ev.target.value;Object(_common_dom_fire_event__WEBPACK_IMPORTED_MODULE_2__.a)(this,"theme-changed")}}],[{key:"properties",get:function(){return{hass:{},value:{}}}}]);return HuiThemeSelectionEditor}(Object(_mixins_lit_localize_mixin__WEBPACK_IMPORTED_MODULE_3__.a)(lit_element__WEBPACK_IMPORTED_MODULE_0__.a));customElements.define("hui-theme-select-editor",HuiThemeSelectionEditor)},212:function(module,__webpack_exports__,__webpack_require__){"use strict";var lit_element__WEBPACK_IMPORTED_MODULE_0__=__webpack_require__(41),_common_dom_fire_event__WEBPACK_IMPORTED_MODULE_1__=__webpack_require__(66),_components_entity_ha_entity_picker__WEBPACK_IMPORTED_MODULE_2__=__webpack_require__(164);function _typeof(obj){if("function"===typeof Symbol&&"symbol"===typeof Symbol.iterator){_typeof=function(obj){return typeof obj}}else{_typeof=function(obj){return obj&&"function"===typeof Symbol&&obj.constructor===Symbol&&obj!==Symbol.prototype?"symbol":typeof obj}}return _typeof(obj)}function _templateObject4(){var data=_taggedTemplateLiteral(["\n      <style>\n        .entities {\n          padding-left: 20px;\n        }\n      </style>\n    "]);_templateObject4=function(){return data};return data}function _templateObject3(){var data=_taggedTemplateLiteral(["\n              <ha-entity-picker\n                .hass=\"","\"\n                .value=\"","\"\n                .index=\"","\"\n                @change=\"","\"\n                allow-custom-entity\n              ></ha-entity-picker>\n            "]);_templateObject3=function(){return data};return data}function _templateObject2(){var data=_taggedTemplateLiteral(["\n      ","\n      <h3>Entities</h3>\n      <div class=\"entities\">\n        ","\n        <ha-entity-picker\n          .hass=\"","\"\n          @change=\"","\"\n        ></ha-entity-picker>\n      </div>\n    "]);_templateObject2=function(){return data};return data}function _templateObject(){var data=_taggedTemplateLiteral([""]);_templateObject=function(){return data};return data}function _taggedTemplateLiteral(strings,raw){if(!raw){raw=strings.slice(0)}return Object.freeze(Object.defineProperties(strings,{raw:{value:Object.freeze(raw)}}))}function _classCallCheck(instance,Constructor){if(!(instance instanceof Constructor)){throw new TypeError("Cannot call a class as a function")}}function _defineProperties(target,props){for(var i=0,descriptor;i<props.length;i++){descriptor=props[i];descriptor.enumerable=descriptor.enumerable||!1;descriptor.configurable=!0;if("value"in descriptor)descriptor.writable=!0;Object.defineProperty(target,descriptor.key,descriptor)}}function _createClass(Constructor,protoProps,staticProps){if(protoProps)_defineProperties(Constructor.prototype,protoProps);if(staticProps)_defineProperties(Constructor,staticProps);return Constructor}function _possibleConstructorReturn(self,call){if(call&&("object"===_typeof(call)||"function"===typeof call)){return call}return _assertThisInitialized(self)}function _assertThisInitialized(self){if(void 0===self){throw new ReferenceError("this hasn't been initialised - super() hasn't been called")}return self}function _getPrototypeOf(o){_getPrototypeOf=Object.setPrototypeOf?Object.getPrototypeOf:function(o){return o.__proto__||Object.getPrototypeOf(o)};return _getPrototypeOf(o)}function _inherits(subClass,superClass){if("function"!==typeof superClass&&null!==superClass){throw new TypeError("Super expression must either be null or a function")}subClass.prototype=Object.create(superClass&&superClass.prototype,{constructor:{value:subClass,writable:!0,configurable:!0}});if(superClass)_setPrototypeOf(subClass,superClass)}function _setPrototypeOf(o,p){_setPrototypeOf=Object.setPrototypeOf||function(o,p){o.__proto__=p;return o};return _setPrototypeOf(o,p)}var HuiEntityEditor=function(_LitElement){_inherits(HuiEntityEditor,_LitElement);function HuiEntityEditor(){_classCallCheck(this,HuiEntityEditor);return _possibleConstructorReturn(this,_getPrototypeOf(HuiEntityEditor).apply(this,arguments))}_createClass(HuiEntityEditor,[{key:"render",value:function(){var _this=this;if(!this.entities){return Object(lit_element__WEBPACK_IMPORTED_MODULE_0__.c)(_templateObject())}return Object(lit_element__WEBPACK_IMPORTED_MODULE_0__.c)(_templateObject2(),this.renderStyle(),this.entities.map(function(entityConf,index){return Object(lit_element__WEBPACK_IMPORTED_MODULE_0__.c)(_templateObject3(),_this.hass,entityConf.entity,index,_this._valueChanged)}),this.hass,this._addEntity)}},{key:"_addEntity",value:function(ev){var target=ev.target;if(""===target.value){return}var newConfigEntities=this.entities.concat({entity:target.value});target.value="";Object(_common_dom_fire_event__WEBPACK_IMPORTED_MODULE_1__.a)(this,"entities-changed",{entities:newConfigEntities})}},{key:"_valueChanged",value:function(ev){var target=ev.target,newConfigEntities=this.entities.concat();if(""===target.value){newConfigEntities.splice(target.index,1)}else{newConfigEntities[target.index]=Object.assign({},newConfigEntities[target.index],{entity:target.value})}Object(_common_dom_fire_event__WEBPACK_IMPORTED_MODULE_1__.a)(this,"entities-changed",{entities:newConfigEntities})}},{key:"renderStyle",value:function(){return Object(lit_element__WEBPACK_IMPORTED_MODULE_0__.c)(_templateObject4())}}],[{key:"properties",get:function(){return{hass:{},entities:{}}}}]);return HuiEntityEditor}(lit_element__WEBPACK_IMPORTED_MODULE_0__.a);customElements.define("hui-entity-editor",HuiEntityEditor)},749:function(module,__webpack_exports__,__webpack_require__){"use strict";__webpack_require__.r(__webpack_exports__);__webpack_require__.d(__webpack_exports__,"HuiGaugeCardEditor",function(){return HuiGaugeCardEditor});var lit_element__WEBPACK_IMPORTED_MODULE_0__=__webpack_require__(41),_polymer_paper_input_paper_input__WEBPACK_IMPORTED_MODULE_1__=__webpack_require__(79),_polymer_paper_toggle_button_paper_toggle_button__WEBPACK_IMPORTED_MODULE_2__=__webpack_require__(187),_common_structs_struct__WEBPACK_IMPORTED_MODULE_3__=__webpack_require__(168),_mixins_lit_localize_mixin__WEBPACK_IMPORTED_MODULE_4__=__webpack_require__(155),_common_dom_fire_event__WEBPACK_IMPORTED_MODULE_5__=__webpack_require__(66),_config_elements_style__WEBPACK_IMPORTED_MODULE_6__=__webpack_require__(171),_components_hui_theme_select_editor__WEBPACK_IMPORTED_MODULE_7__=__webpack_require__(207),_components_hui_entity_editor__WEBPACK_IMPORTED_MODULE_8__=__webpack_require__(212);function _typeof(obj){if("function"===typeof Symbol&&"symbol"===typeof Symbol.iterator){_typeof=function(obj){return typeof obj}}else{_typeof=function(obj){return obj&&"function"===typeof Symbol&&obj.constructor===Symbol&&obj!==Symbol.prototype?"symbol":typeof obj}}return _typeof(obj)}function _defineProperty(obj,key,value){if(key in obj){Object.defineProperty(obj,key,{value:value,enumerable:!0,configurable:!0,writable:!0})}else{obj[key]=value}return obj}function _templateObject3(){var data=_taggedTemplateLiteral(["\n      <style>\n        .severity {\n          display: none;\n          width: 100%;\n          padding-left: 16px;\n          flex-direction: row;\n          flex-wrap: wrap;\n        }\n        .severity > * {\n          flex: 1 0 30%;\n          padding-right: 4px;\n        }\n        paper-toggle-button[checked] ~ .severity {\n          display: flex;\n        }\n      </style>\n    "]);_templateObject3=function(){return data};return data}function _templateObject2(){var data=_taggedTemplateLiteral(["\n      "," ","\n      <div class=\"card-config\">\n        <div class=\"side-by-side\">\n          <paper-input\n            label=\"Name\"\n            .value=\"","\"\n            .configValue=","\n            @value-changed=\"","\"\n          ></paper-input>\n          <ha-entity-picker\n            .hass=\"","\"\n            .value=\"","\"\n            .configValue=","\n            domain-filter=\"sensor\"\n            @change=\"","\"\n            allow-custom-entity\n          ></ha-entity-picker>\n        </div>\n        <div class=\"side-by-side\">\n          <paper-input\n            label=\"Unit\"\n            .value=\"","\"\n            .configValue=","\n            @value-changed=\"","\"\n          ></paper-input>\n          <hui-theme-select-editor\n            .hass=\"","\"\n            .value=\"","\"\n            .configValue=\"","\"\n            @theme-changed=\"","\"\n          ></hui-theme-select-editor>\n        </div>\n        <div class=\"side-by-side\">\n          <paper-input\n            type=\"number\"\n            label=\"Minimum\"\n            .value=\"","\"\n            .configValue=","\n            @value-changed=\"","\"\n          ></paper-input>\n          <paper-input\n            type=\"number\"\n            label=\"Maximum\"\n            .value=\"","\"\n            .configValue=","\n            @value-changed=\"","\"\n          ></paper-input>\n        </div>\n        <div class=\"side-by-side\">\n          <paper-toggle-button\n            ?checked=\"","\"\n            @change=\"","\"\n            >Define Severity?</paper-toggle-button\n          >\n          <div class=\"severity\">\n            <paper-input\n              type=\"number\"\n              label=\"Green\"\n              .value=\"","\"\n              .configValue=","\n              @value-changed=\"","\"\n            ></paper-input>\n            <paper-input\n              type=\"number\"\n              label=\"Yellow\"\n              .value=\"","\"\n              .configValue=","\n              @value-changed=\"","\"\n            ></paper-input>\n            <paper-input\n              type=\"number\"\n              label=\"Red\"\n              .value=\"","\"\n              .configValue=","\n              @value-changed=\"","\"\n            ></paper-input>\n          </div>\n        </div>\n      </div>\n    "]);_templateObject2=function(){return data};return data}function _templateObject(){var data=_taggedTemplateLiteral([""]);_templateObject=function(){return data};return data}function _taggedTemplateLiteral(strings,raw){if(!raw){raw=strings.slice(0)}return Object.freeze(Object.defineProperties(strings,{raw:{value:Object.freeze(raw)}}))}function _classCallCheck(instance,Constructor){if(!(instance instanceof Constructor)){throw new TypeError("Cannot call a class as a function")}}function _defineProperties(target,props){for(var i=0,descriptor;i<props.length;i++){descriptor=props[i];descriptor.enumerable=descriptor.enumerable||!1;descriptor.configurable=!0;if("value"in descriptor)descriptor.writable=!0;Object.defineProperty(target,descriptor.key,descriptor)}}function _createClass(Constructor,protoProps,staticProps){if(protoProps)_defineProperties(Constructor.prototype,protoProps);if(staticProps)_defineProperties(Constructor,staticProps);return Constructor}function _possibleConstructorReturn(self,call){if(call&&("object"===_typeof(call)||"function"===typeof call)){return call}return _assertThisInitialized(self)}function _assertThisInitialized(self){if(void 0===self){throw new ReferenceError("this hasn't been initialised - super() hasn't been called")}return self}function _getPrototypeOf(o){_getPrototypeOf=Object.setPrototypeOf?Object.getPrototypeOf:function(o){return o.__proto__||Object.getPrototypeOf(o)};return _getPrototypeOf(o)}function _inherits(subClass,superClass){if("function"!==typeof superClass&&null!==superClass){throw new TypeError("Super expression must either be null or a function")}subClass.prototype=Object.create(superClass&&superClass.prototype,{constructor:{value:subClass,writable:!0,configurable:!0}});if(superClass)_setPrototypeOf(subClass,superClass)}function _setPrototypeOf(o,p){_setPrototypeOf=Object.setPrototypeOf||function(o,p){o.__proto__=p;return o};return _setPrototypeOf(o,p)}var cardConfigStruct=Object(_common_structs_struct__WEBPACK_IMPORTED_MODULE_3__.a)({type:"string",name:"string?",entity:"string?",unit:"string?",min:"number?",max:"number?",severity:"object?",theme:"string?"}),HuiGaugeCardEditor=function(_hassLocalizeLitMixin){_inherits(HuiGaugeCardEditor,_hassLocalizeLitMixin);function HuiGaugeCardEditor(){_classCallCheck(this,HuiGaugeCardEditor);return _possibleConstructorReturn(this,_getPrototypeOf(HuiGaugeCardEditor).apply(this,arguments))}_createClass(HuiGaugeCardEditor,[{key:"setConfig",value:function(config){config=cardConfigStruct(config);this._useSeverity=config.severity?!0:!1;this._config=config}},{key:"render",value:function(){if(!this.hass){return Object(lit_element__WEBPACK_IMPORTED_MODULE_0__.c)(_templateObject())}return Object(lit_element__WEBPACK_IMPORTED_MODULE_0__.c)(_templateObject2(),_config_elements_style__WEBPACK_IMPORTED_MODULE_6__.a,this.renderStyle(),this._name,"name",this._valueChanged,this.hass,this._entity,"entity",this._valueChanged,this._unit,"unit",this._valueChanged,this.hass,this._theme,"theme",this._valueChanged,this._min,"min",this._valueChanged,this._max,"max",this._valueChanged,!1!==this._useSeverity,this._toggleSeverity,this._severity?this._severity.green:0,"green",this._severityChanged,this._severity?this._severity.yellow:0,"yellow",this._severityChanged,this._severity?this._severity.red:0,"red",this._severityChanged)}},{key:"renderStyle",value:function(){return Object(lit_element__WEBPACK_IMPORTED_MODULE_0__.c)(_templateObject3())}},{key:"_toggleSeverity",value:function(ev){if(!this._config||!this.hass){return}var target=ev.target;this._config.severity=target.checked?{green:0,yellow:0,red:0}:void 0;Object(_common_dom_fire_event__WEBPACK_IMPORTED_MODULE_5__.a)(this,"config-changed",{config:this._config})}},{key:"_severityChanged",value:function(ev){if(!this._config||!this.hass){return}var target=ev.target,severity=Object.assign({},this._config.severity,_defineProperty({},target.configValue,+target.value));this._config=Object.assign({},this._config,{severity:severity});Object(_common_dom_fire_event__WEBPACK_IMPORTED_MODULE_5__.a)(this,"config-changed",{config:this._config})}},{key:"_valueChanged",value:function(ev){if(!this._config||!this.hass){return}var target=ev.target;if(target.configValue){if(""===target.value||"number"===target.type&&isNaN(+target.value)){delete this._config[target.configValue]}else{var value=target.value;if("number"===target.type){value=+value}this._config=Object.assign({},this._config,_defineProperty({},target.configValue,value))}}Object(_common_dom_fire_event__WEBPACK_IMPORTED_MODULE_5__.a)(this,"config-changed",{config:this._config})}},{key:"_name",get:function(){return this._config.name||""}},{key:"_entity",get:function(){return this._config.entity||""}},{key:"_unit",get:function(){return this._config.unit||""}},{key:"_theme",get:function(){return this._config.theme||"default"}},{key:"_min",get:function(){return this._config.number||0}},{key:"_max",get:function(){return this._config.max||100}},{key:"_severity",get:function(){return this._config.severity||void 0}}],[{key:"properties",get:function(){return{hass:{},_config:{}}}}]);return HuiGaugeCardEditor}(Object(_mixins_lit_localize_mixin__WEBPACK_IMPORTED_MODULE_4__.a)(lit_element__WEBPACK_IMPORTED_MODULE_0__.a));customElements.define("hui-gauge-card-editor",HuiGaugeCardEditor)}}]);
//# sourceMappingURL=9a8d2fdea1625a683a19.chunk.js.map