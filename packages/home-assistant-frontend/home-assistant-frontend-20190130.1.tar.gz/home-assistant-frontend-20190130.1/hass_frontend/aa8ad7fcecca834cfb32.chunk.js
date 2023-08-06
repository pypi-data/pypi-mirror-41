(window.webpackJsonp=window.webpackJsonp||[]).push([[38],{165:function(module,__webpack_exports__,__webpack_require__){"use strict";var _polymer_paper_icon_button_paper_icon_button__WEBPACK_IMPORTED_MODULE_0__=__webpack_require__(99),_polymer_paper_input_paper_input__WEBPACK_IMPORTED_MODULE_1__=__webpack_require__(78),_polymer_paper_item_paper_icon_item__WEBPACK_IMPORTED_MODULE_2__=__webpack_require__(164),_polymer_paper_item_paper_item_body__WEBPACK_IMPORTED_MODULE_3__=__webpack_require__(156),_polymer_polymer_lib_utils_html_tag__WEBPACK_IMPORTED_MODULE_4__=__webpack_require__(2),_polymer_polymer_polymer_element__WEBPACK_IMPORTED_MODULE_5__=__webpack_require__(12),_vaadin_vaadin_combo_box_vaadin_combo_box_light__WEBPACK_IMPORTED_MODULE_6__=__webpack_require__(185),_state_badge__WEBPACK_IMPORTED_MODULE_7__=__webpack_require__(163),_common_entity_compute_state_name__WEBPACK_IMPORTED_MODULE_8__=__webpack_require__(106),_mixins_localize_mixin__WEBPACK_IMPORTED_MODULE_9__=__webpack_require__(105),_mixins_events_mixin__WEBPACK_IMPORTED_MODULE_10__=__webpack_require__(53);class HaEntityPicker extends Object(_mixins_events_mixin__WEBPACK_IMPORTED_MODULE_10__.a)(Object(_mixins_localize_mixin__WEBPACK_IMPORTED_MODULE_9__.a)(_polymer_polymer_polymer_element__WEBPACK_IMPORTED_MODULE_5__.a)){static get template(){return _polymer_polymer_lib_utils_html_tag__WEBPACK_IMPORTED_MODULE_4__.a`
      <style>
        paper-input > paper-icon-button {
          width: 24px;
          height: 24px;
          padding: 2px;
          color: var(--secondary-text-color);
        }
        [hidden] {
          display: none;
        }
      </style>
      <vaadin-combo-box-light
        items="[[_states]]"
        item-value-path="entity_id"
        item-label-path="entity_id"
        value="{{value}}"
        opened="{{opened}}"
        allow-custom-value="[[allowCustomEntity]]"
        on-change="_fireChanged"
      >
        <paper-input
          autofocus="[[autofocus]]"
          label="[[_computeLabel(label, localize)]]"
          class="input"
          autocapitalize="none"
          autocomplete="off"
          autocorrect="off"
          spellcheck="false"
          value="[[value]]"
          disabled="[[disabled]]"
        >
          <paper-icon-button
            slot="suffix"
            class="clear-button"
            icon="hass:close"
            no-ripple=""
            hidden$="[[!value]]"
            >Clear</paper-icon-button
          >
          <paper-icon-button
            slot="suffix"
            class="toggle-button"
            icon="[[_computeToggleIcon(opened)]]"
            hidden="[[!_states.length]]"
            >Toggle</paper-icon-button
          >
        </paper-input>
        <template>
          <style>
            paper-icon-item {
              margin: -10px;
              padding: 0;
            }
          </style>
          <paper-icon-item>
            <state-badge state-obj="[[item]]" slot="item-icon"></state-badge>
            <paper-item-body two-line="">
              <div>[[_computeStateName(item)]]</div>
              <div secondary="">[[item.entity_id]]</div>
            </paper-item-body>
          </paper-icon-item>
        </template>
      </vaadin-combo-box-light>
    `}static get properties(){return{allowCustomEntity:{type:Boolean,value:!1},hass:{type:Object,observer:"_hassChanged"},_hass:Object,_states:{type:Array,computed:"_computeStates(_hass, domainFilter, entityFilter)"},autofocus:Boolean,label:{type:String},value:{type:String,notify:!0},opened:{type:Boolean,value:!1,observer:"_openedChanged"},domainFilter:{type:String,value:null},entityFilter:{type:Function,value:null},disabled:Boolean}}_computeLabel(label,localize){return label===void 0?localize("ui.components.entity.entity-picker.entity"):label}_computeStates(hass,domainFilter,entityFilter){if(!hass)return[];let entityIds=Object.keys(hass.states);if(domainFilter){entityIds=entityIds.filter(eid=>eid.substr(0,eid.indexOf("."))===domainFilter)}let entities=entityIds.sort().map(key=>hass.states[key]);if(entityFilter){entities=entities.filter(entityFilter)}return entities}_computeStateName(state){return Object(_common_entity_compute_state_name__WEBPACK_IMPORTED_MODULE_8__.a)(state)}_openedChanged(newVal){if(!newVal){this._hass=this.hass}}_hassChanged(newVal){if(!this.opened){this._hass=newVal}}_computeToggleIcon(opened){return opened?"hass:menu-up":"hass:menu-down"}_fireChanged(ev){ev.stopPropagation();this.fire("change")}}customElements.define("ha-entity-picker",HaEntityPicker)},167:function(module,__webpack_exports__,__webpack_require__){"use strict";var index_es=__webpack_require__(171);function isEntityId(value){if("string"!==typeof value){return"entity id should be a string"}if(!value.includes(".")){return"entity id should be in the format 'domain.entity'"}return!0}function isIcon(value){if("string"!==typeof value){return"icon should be a string"}if(!value.includes(":")){return"icon should be in the format 'mdi:icon'"}return!0}__webpack_require__.d(__webpack_exports__,"a",function(){return struct});const struct=Object(index_es.a)({types:{"entity-id":isEntityId,icon:isIcon}})},174:function(module,__webpack_exports__,__webpack_require__){"use strict";__webpack_require__.d(__webpack_exports__,"a",function(){return configElementStyle});var lit_element__WEBPACK_IMPORTED_MODULE_0__=__webpack_require__(20);const configElementStyle=lit_element__WEBPACK_IMPORTED_MODULE_0__.c`
  <style>
    paper-toggle-button {
      padding-top: 16px;
    }
    .side-by-side {
      display: flex;
    }
    .side-by-side > * {
      flex: 1;
      padding-right: 4px;
    }
  </style>
`},213:function(module,__webpack_exports__,__webpack_require__){"use strict";var lit_element__WEBPACK_IMPORTED_MODULE_0__=__webpack_require__(20),_common_dom_fire_event__WEBPACK_IMPORTED_MODULE_1__=__webpack_require__(66),_components_entity_ha_entity_picker__WEBPACK_IMPORTED_MODULE_2__=__webpack_require__(165);class HuiEntityEditor extends lit_element__WEBPACK_IMPORTED_MODULE_0__.a{static get properties(){return{hass:{},entities:{}}}render(){if(!this.entities){return lit_element__WEBPACK_IMPORTED_MODULE_0__.c``}return lit_element__WEBPACK_IMPORTED_MODULE_0__.c`
      ${this.renderStyle()}
      <h3>Entities</h3>
      <div class="entities">
        ${this.entities.map((entityConf,index)=>{return lit_element__WEBPACK_IMPORTED_MODULE_0__.c`
            <ha-entity-picker
              .hass="${this.hass}"
              .value="${entityConf.entity}"
              .index="${index}"
              @change="${this._valueChanged}"
              allow-custom-entity
            ></ha-entity-picker>
          `})}
        <ha-entity-picker
          .hass="${this.hass}"
          @change="${this._addEntity}"
        ></ha-entity-picker>
      </div>
    `}_addEntity(ev){const target=ev.target;if(""===target.value){return}const newConfigEntities=this.entities.concat({entity:target.value});target.value="";Object(_common_dom_fire_event__WEBPACK_IMPORTED_MODULE_1__.a)(this,"entities-changed",{entities:newConfigEntities})}_valueChanged(ev){const target=ev.target,newConfigEntities=this.entities.concat();if(""===target.value){newConfigEntities.splice(target.index,1)}else{newConfigEntities[target.index]=Object.assign({},newConfigEntities[target.index],{entity:target.value})}Object(_common_dom_fire_event__WEBPACK_IMPORTED_MODULE_1__.a)(this,"entities-changed",{entities:newConfigEntities})}renderStyle(){return lit_element__WEBPACK_IMPORTED_MODULE_0__.c`
      <style>
        .entities {
          padding-left: 20px;
        }
      </style>
    `}}customElements.define("hui-entity-editor",HuiEntityEditor)},259:function(module,__webpack_exports__,__webpack_require__){"use strict";__webpack_require__.d(__webpack_exports__,"a",function(){return processEditorEntities});function processEditorEntities(entities){return entities.map(entityConf=>{if("string"===typeof entityConf){return{entity:entityConf}}return entityConf})}},747:function(module,__webpack_exports__,__webpack_require__){"use strict";__webpack_require__.r(__webpack_exports__);__webpack_require__.d(__webpack_exports__,"HuiMapCardEditor",function(){return HuiMapCardEditor});var lit_element__WEBPACK_IMPORTED_MODULE_0__=__webpack_require__(20),_polymer_paper_input_paper_input__WEBPACK_IMPORTED_MODULE_1__=__webpack_require__(78),_common_structs_struct__WEBPACK_IMPORTED_MODULE_2__=__webpack_require__(167),_common_dom_fire_event__WEBPACK_IMPORTED_MODULE_3__=__webpack_require__(66),_config_elements_style__WEBPACK_IMPORTED_MODULE_4__=__webpack_require__(174),_process_editor_entities__WEBPACK_IMPORTED_MODULE_5__=__webpack_require__(259),_components_hui_entity_editor__WEBPACK_IMPORTED_MODULE_6__=__webpack_require__(213);const entitiesConfigStruct=_common_structs_struct__WEBPACK_IMPORTED_MODULE_2__.a.union([{entity:"entity-id",name:"string?",icon:"icon?"},"entity-id"]),cardConfigStruct=Object(_common_structs_struct__WEBPACK_IMPORTED_MODULE_2__.a)({type:"string",title:"string?",aspect_ratio:"string?",default_zoom:"number?",entities:[entitiesConfigStruct]});class HuiMapCardEditor extends lit_element__WEBPACK_IMPORTED_MODULE_0__.a{setConfig(config){config=cardConfigStruct(config);this._config=config;this._configEntities=Object(_process_editor_entities__WEBPACK_IMPORTED_MODULE_5__.a)(config.entities)}static get properties(){return{hass:{},_config:{},_configEntities:{}}}get _title(){return this._config.title||""}get _aspect_ratio(){return this._config.aspect_ratio||""}get _default_zoom(){return this._config.default_zoom||NaN}get _entities(){return this._config.entities||[]}render(){if(!this.hass){return lit_element__WEBPACK_IMPORTED_MODULE_0__.c``}return lit_element__WEBPACK_IMPORTED_MODULE_0__.c`
      ${_config_elements_style__WEBPACK_IMPORTED_MODULE_4__.a}
      <div class="card-config">
        <paper-input
          label="Title"
          .value="${this._title}"
          .configValue="${"title"}"
          @value-changed="${this._valueChanged}"
        ></paper-input>
        <div class="side-by-side">
          <paper-input
            label="Aspect Ratio"
            .value="${this._aspect_ratio}"
            .configValue="${"aspect_ratio"}"
            @value-changed="${this._valueChanged}"
          ></paper-input>
          <paper-input
            label="Default Zoom"
            type="number"
            .value="${this._default_zoom}"
            .configValue="${"default_zoom"}"
            @value-changed="${this._valueChanged}"
          ></paper-input>
        </div>
        <hui-entity-editor
          .hass="${this.hass}"
          .entities="${this._configEntities}"
          @entities-changed="${this._valueChanged}"
        ></hui-entity-editor>
      </div>
    `}_valueChanged(ev){if(!this._config||!this.hass){return}const target=ev.target;if(target.configValue&&this[`_${target.configValue}`]===target.value){return}if(ev.detail&&ev.detail.entities){this._config.entities=ev.detail.entities;this._configEntities=Object(_process_editor_entities__WEBPACK_IMPORTED_MODULE_5__.a)(this._config.entities)}else if(target.configValue){if(""===target.value||"number"===target.type&&isNaN(+target.value)){delete this._config[target.configValue]}else{let value=target.value;if("number"===target.type){value=+value}this._config=Object.assign({},this._config,{[target.configValue]:value})}}Object(_common_dom_fire_event__WEBPACK_IMPORTED_MODULE_3__.a)(this,"config-changed",{config:this._config})}}customElements.define("hui-map-card-editor",HuiMapCardEditor)}}]);
//# sourceMappingURL=aa8ad7fcecca834cfb32.chunk.js.map