(window.webpackJsonp=window.webpackJsonp||[]).push([[78],{163:function(module,__webpack_exports__,__webpack_require__){"use strict";var _polymer_paper_icon_button_paper_icon_button__WEBPACK_IMPORTED_MODULE_0__=__webpack_require__(98),_polymer_paper_input_paper_input__WEBPACK_IMPORTED_MODULE_1__=__webpack_require__(79),_polymer_paper_item_paper_icon_item__WEBPACK_IMPORTED_MODULE_2__=__webpack_require__(162),_polymer_paper_item_paper_item_body__WEBPACK_IMPORTED_MODULE_3__=__webpack_require__(155),_polymer_polymer_lib_utils_html_tag__WEBPACK_IMPORTED_MODULE_4__=__webpack_require__(1),_polymer_polymer_polymer_element__WEBPACK_IMPORTED_MODULE_5__=__webpack_require__(11),_vaadin_vaadin_combo_box_vaadin_combo_box_light__WEBPACK_IMPORTED_MODULE_6__=__webpack_require__(182),_state_badge__WEBPACK_IMPORTED_MODULE_7__=__webpack_require__(161),_common_entity_compute_state_name__WEBPACK_IMPORTED_MODULE_8__=__webpack_require__(105),_mixins_localize_mixin__WEBPACK_IMPORTED_MODULE_9__=__webpack_require__(72),_mixins_events_mixin__WEBPACK_IMPORTED_MODULE_10__=__webpack_require__(50);class HaEntityPicker extends Object(_mixins_events_mixin__WEBPACK_IMPORTED_MODULE_10__.a)(Object(_mixins_localize_mixin__WEBPACK_IMPORTED_MODULE_9__.a)(_polymer_polymer_polymer_element__WEBPACK_IMPORTED_MODULE_5__.a)){static get template(){return _polymer_polymer_lib_utils_html_tag__WEBPACK_IMPORTED_MODULE_4__.a`
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
    `}static get properties(){return{allowCustomEntity:{type:Boolean,value:!1},hass:{type:Object,observer:"_hassChanged"},_hass:Object,_states:{type:Array,computed:"_computeStates(_hass, domainFilter, entityFilter)"},autofocus:Boolean,label:{type:String},value:{type:String,notify:!0},opened:{type:Boolean,value:!1,observer:"_openedChanged"},domainFilter:{type:String,value:null},entityFilter:{type:Function,value:null},disabled:Boolean}}_computeLabel(label,localize){return label===void 0?localize("ui.components.entity.entity-picker.entity"):label}_computeStates(hass,domainFilter,entityFilter){if(!hass)return[];let entityIds=Object.keys(hass.states);if(domainFilter){entityIds=entityIds.filter(eid=>eid.substr(0,eid.indexOf("."))===domainFilter)}let entities=entityIds.sort().map(key=>hass.states[key]);if(entityFilter){entities=entities.filter(entityFilter)}return entities}_computeStateName(state){return Object(_common_entity_compute_state_name__WEBPACK_IMPORTED_MODULE_8__.a)(state)}_openedChanged(newVal){if(!newVal){this._hass=this.hass}}_hassChanged(newVal){if(!this.opened){this._hass=newVal}}_computeToggleIcon(opened){return opened?"hass:menu-up":"hass:menu-down"}_fireChanged(ev){ev.stopPropagation();this.fire("change")}}customElements.define("ha-entity-picker",HaEntityPicker)},166:function(module,__webpack_exports__,__webpack_require__){"use strict";var index_es=__webpack_require__(169);__webpack_require__.d(__webpack_exports__,"a",function(){return struct});const struct=Object(index_es.a)({types:{"entity-id":function(value){if("string"!==typeof value){return"entity id should be a string"}if(!value.includes(".")){return"entity id should be in the format 'domain.entity'"}return!0},icon:function(value){if("string"!==typeof value){return"icon should be a string"}if(!value.includes(":")){return"icon should be in the format 'mdi:icon'"}return!0}}})},171:function(module,__webpack_exports__,__webpack_require__){"use strict";__webpack_require__.d(__webpack_exports__,"a",function(){return configElementStyle});var lit_element__WEBPACK_IMPORTED_MODULE_0__=__webpack_require__(31);const configElementStyle=lit_element__WEBPACK_IMPORTED_MODULE_0__.c`
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
`},206:function(module,__webpack_exports__,__webpack_require__){"use strict";var lit_element__WEBPACK_IMPORTED_MODULE_0__=__webpack_require__(31),_polymer_paper_button_paper_button__WEBPACK_IMPORTED_MODULE_1__=__webpack_require__(73),_common_dom_fire_event__WEBPACK_IMPORTED_MODULE_2__=__webpack_require__(66),_mixins_lit_localize_mixin__WEBPACK_IMPORTED_MODULE_3__=__webpack_require__(154);class HuiThemeSelectionEditor extends Object(_mixins_lit_localize_mixin__WEBPACK_IMPORTED_MODULE_3__.a)(lit_element__WEBPACK_IMPORTED_MODULE_0__.a){static get properties(){return{hass:{},value:{}}}render(){const themes=["Backend-selected","default"].concat(Object.keys(this.hass.themes.themes).sort());return lit_element__WEBPACK_IMPORTED_MODULE_0__.c`
      ${this.renderStyle()}
      <paper-dropdown-menu
        label="Theme"
        dynamic-align
        @value-changed="${this._changed}"
      >
        <paper-listbox
          slot="dropdown-content"
          .selected="${this.value}"
          attr-for-selected="theme"
        >
          ${themes.map(theme=>{return lit_element__WEBPACK_IMPORTED_MODULE_0__.c`
                <paper-item theme="${theme}">${theme}</paper-item>
              `})}
        </paper-listbox>
      </paper-dropdown-menu>
    `}renderStyle(){return lit_element__WEBPACK_IMPORTED_MODULE_0__.c`
      <style>
        paper-dropdown-menu {
          width: 100%;
        }
      </style>
    `}_changed(ev){if(!this.hass||""===ev.target.value){return}this.value=ev.target.value;Object(_common_dom_fire_event__WEBPACK_IMPORTED_MODULE_2__.a)(this,"theme-changed")}}customElements.define("hui-theme-select-editor",HuiThemeSelectionEditor)},745:function(module,__webpack_exports__,__webpack_require__){"use strict";__webpack_require__.r(__webpack_exports__);__webpack_require__.d(__webpack_exports__,"HuiSensorCardEditor",function(){return HuiSensorCardEditor});var lit_element__WEBPACK_IMPORTED_MODULE_0__=__webpack_require__(31),_polymer_paper_input_paper_input__WEBPACK_IMPORTED_MODULE_1__=__webpack_require__(79),_polymer_paper_dropdown_menu_paper_dropdown_menu__WEBPACK_IMPORTED_MODULE_2__=__webpack_require__(128),_polymer_paper_item_paper_item__WEBPACK_IMPORTED_MODULE_3__=__webpack_require__(125),_polymer_paper_listbox_paper_listbox__WEBPACK_IMPORTED_MODULE_4__=__webpack_require__(127),_common_structs_struct__WEBPACK_IMPORTED_MODULE_5__=__webpack_require__(166),_mixins_lit_localize_mixin__WEBPACK_IMPORTED_MODULE_6__=__webpack_require__(154),_common_dom_fire_event__WEBPACK_IMPORTED_MODULE_7__=__webpack_require__(66),_config_elements_style__WEBPACK_IMPORTED_MODULE_8__=__webpack_require__(171),_components_hui_theme_select_editor__WEBPACK_IMPORTED_MODULE_9__=__webpack_require__(206),_components_entity_ha_entity_picker__WEBPACK_IMPORTED_MODULE_10__=__webpack_require__(163);const cardConfigStruct=Object(_common_structs_struct__WEBPACK_IMPORTED_MODULE_5__.a)({type:"string",entity:"string?",name:"string?",icon:"string?",graph:"string?",unit:"string?",detail:"number?",theme:"string?",hours_to_show:"number?"});class HuiSensorCardEditor extends Object(_mixins_lit_localize_mixin__WEBPACK_IMPORTED_MODULE_6__.a)(lit_element__WEBPACK_IMPORTED_MODULE_0__.a){setConfig(config){config=cardConfigStruct(config);this._config=config}static get properties(){return{hass:{},_config:{}}}get _entity(){return this._config.entity||""}get _name(){return this._config.name||""}get _icon(){return this._config.icon||""}get _graph(){return this._config.graph||"none"}get _unit(){return this._config.unit||""}get _detail(){return this._config.number||"1"}get _theme(){return this._config.theme||"default"}get _hours_to_show(){return this._config.hours_to_show||"24"}render(){if(!this.hass){return lit_element__WEBPACK_IMPORTED_MODULE_0__.c``}const graphs=["line","none"];return lit_element__WEBPACK_IMPORTED_MODULE_0__.c`
      ${_config_elements_style__WEBPACK_IMPORTED_MODULE_8__.a}
      <div class="card-config">
        <div class="side-by-side">
          <paper-input
            label="Name"
            .value="${this._name}"
            .configValue="${"name"}"
            @value-changed="${this._valueChanged}"
          ></paper-input>
          <ha-entity-picker
            .hass="${this.hass}"
            .value="${this._entity}"
            .configValue=${"entity"}
            domain-filter="sensor"
            @change="${this._valueChanged}"
            allow-custom-entity
          ></ha-entity-picker>
        </div>
        <div class="side-by-side">
          <paper-input
            label="Icon"
            .value="${this._icon}"
            .configValue="${"icon"}"
            @value-changed="${this._valueChanged}"
          ></paper-input>
          <paper-dropdown-menu
            label="Graph Type"
            .configValue="${"graph"}"
            @value-changed="${this._valueChanged}"
          >
            <paper-listbox
              slot="dropdown-content"
              .selected="${graphs.indexOf(this._graph)}"
            >
              ${graphs.map(graph=>{return lit_element__WEBPACK_IMPORTED_MODULE_0__.c`
                    <paper-item>${graph}</paper-item>
                  `})}
            </paper-listbox>
          </paper-dropdown-menu>
        </div>
        <div class="side-by-side">
          <paper-input
            label="Units"
            .value="${this._unit}"
            .configValue="${"unit"}"
            @value-changed="${this._valueChanged}"
          ></paper-input>
          <paper-input
            label="Graph Detail"
            type="number"
            .value="${this._detail}"
            .configValue="${"detail"}"
            @value-changed="${this._valueChanged}"
          ></paper-input>
        </div>
        <div class="side-by-side">
          <hui-theme-select-editor
            .hass="${this.hass}"
            .value="${this._theme}"
            .configValue="${"theme"}"
            @theme-changed="${this._valueChanged}"
          ></hui-theme-select-editor>
          <paper-input
            label="Hours To Show"
            type="number"
            .value="${this._hours_to_show}"
            .configValue="${"hours_to_show"}"
            @value-changed="${this._valueChanged}"
          ></paper-input>
        </div>
      </div>
    `}_valueChanged(ev){if(!this._config||!this.hass){return}const target=ev.target;if(this[`_${target.configValue}`]===target.value){return}if(target.configValue){if(""===target.value||"number"===target.type&&isNaN(+target.value)){delete this._config[target.configValue]}else{let value=target.value;if("number"===target.type){value=+value}this._config=Object.assign({},this._config,{[target.configValue]:value})}}Object(_common_dom_fire_event__WEBPACK_IMPORTED_MODULE_7__.a)(this,"config-changed",{config:this._config})}}customElements.define("hui-sensor-card-editor",HuiSensorCardEditor)}}]);
//# sourceMappingURL=41275c0e002a372a996e.chunk.js.map