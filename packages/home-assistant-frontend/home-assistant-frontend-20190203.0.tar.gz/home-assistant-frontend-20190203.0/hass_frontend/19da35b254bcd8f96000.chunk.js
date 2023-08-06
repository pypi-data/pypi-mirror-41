(window.webpackJsonp=window.webpackJsonp||[]).push([[62],{169:function(module,__webpack_exports__,__webpack_require__){"use strict";var _polymer_polymer_lib_utils_html_tag__WEBPACK_IMPORTED_MODULE_0__=__webpack_require__(2),_polymer_polymer_polymer_element__WEBPACK_IMPORTED_MODULE_1__=__webpack_require__(12),_resources_ha_style__WEBPACK_IMPORTED_MODULE_2__=__webpack_require__(96);class HaConfigSection extends _polymer_polymer_polymer_element__WEBPACK_IMPORTED_MODULE_1__.a{static get template(){return _polymer_polymer_lib_utils_html_tag__WEBPACK_IMPORTED_MODULE_0__.a`
      <style include="iron-flex ha-style">
        .content {
          padding: 28px 20px 0;
          max-width: 1040px;
          margin: 0 auto;
        }

        .header {
          @apply --paper-font-display1;
          opacity: var(--dark-primary-opacity);
        }

        .together {
          margin-top: 32px;
        }

        .intro {
          @apply --paper-font-subhead;
          width: 100%;
          max-width: 400px;
          margin-right: 40px;
          opacity: var(--dark-primary-opacity);
        }

        .panel {
          margin-top: -24px;
        }

        .panel ::slotted(*) {
          margin-top: 24px;
          display: block;
        }

        .narrow.content {
          max-width: 640px;
        }
        .narrow .together {
          margin-top: 20px;
        }
        .narrow .header {
          @apply --paper-font-headline;
        }
        .narrow .intro {
          font-size: 14px;
          padding-bottom: 20px;
          margin-right: 0;
          max-width: 500px;
        }
      </style>
      <div class$="[[computeContentClasses(isWide)]]">
        <div class="header"><slot name="header"></slot></div>
        <div class$="[[computeClasses(isWide)]]">
          <div class="intro"><slot name="introduction"></slot></div>
          <div class="panel flex-auto"><slot></slot></div>
        </div>
      </div>
    `}static get properties(){return{hass:{type:Object},narrow:{type:Boolean},showMenu:{type:Boolean,value:!1},isWide:{type:Boolean,value:!1}}}computeContentClasses(isWide){var classes="content ";return isWide?classes:classes+"narrow"}computeClasses(isWide){var classes="together layout ";return classes+(isWide?"horizontal":"vertical narrow")}}customElements.define("ha-config-section",HaConfigSection)},196:function(module,__webpack_exports__,__webpack_require__){"use strict";var _polymer_app_layout_app_header_layout_app_header_layout__WEBPACK_IMPORTED_MODULE_0__=__webpack_require__(176),_polymer_app_layout_app_header_app_header__WEBPACK_IMPORTED_MODULE_1__=__webpack_require__(171),_polymer_app_layout_app_toolbar_app_toolbar__WEBPACK_IMPORTED_MODULE_2__=__webpack_require__(126),_polymer_paper_icon_button_paper_icon_button__WEBPACK_IMPORTED_MODULE_3__=__webpack_require__(93),_polymer_polymer_lib_utils_html_tag__WEBPACK_IMPORTED_MODULE_4__=__webpack_require__(2),_polymer_polymer_polymer_element__WEBPACK_IMPORTED_MODULE_5__=__webpack_require__(12);class HassSubpage extends _polymer_polymer_polymer_element__WEBPACK_IMPORTED_MODULE_5__.a{static get template(){return _polymer_polymer_lib_utils_html_tag__WEBPACK_IMPORTED_MODULE_4__.a`
      <style include="ha-style"></style>
      <app-header-layout has-scrolling-region="">
        <app-header slot="header" fixed="">
          <app-toolbar>
            <paper-icon-button
              icon="hass:arrow-left"
              on-click="_backTapped"
            ></paper-icon-button>
            <div main-title="">[[header]]</div>
            <slot name="toolbar-icon"></slot>
          </app-toolbar>
        </app-header>

        <slot></slot>
      </app-header-layout>
    `}static get properties(){return{header:String}}_backTapped(){history.back()}}customElements.define("hass-subpage",HassSubpage)},255:function(module,__webpack_exports__,__webpack_require__){"use strict";__webpack_exports__.a=(a,b)=>{if(a<b){return-1}if(a>b){return 1}return 0}},369:function(module,__webpack_exports__,__webpack_require__){"use strict";__webpack_require__.d(__webpack_exports__,"c",function(){return fetchAreaRegistry});__webpack_require__.d(__webpack_exports__,"a",function(){return createAreaRegistryEntry});__webpack_require__.d(__webpack_exports__,"d",function(){return updateAreaRegistryEntry});__webpack_require__.d(__webpack_exports__,"b",function(){return deleteAreaRegistryEntry});const fetchAreaRegistry=hass=>hass.callWS({type:"config/area_registry/list"}),createAreaRegistryEntry=(hass,values)=>hass.callWS(Object.assign({type:"config/area_registry/create"},values)),updateAreaRegistryEntry=(hass,areaId,updates)=>hass.callWS(Object.assign({type:"config/area_registry/update",area_id:areaId},updates)),deleteAreaRegistryEntry=(hass,areaId)=>hass.callWS({type:"config/area_registry/delete",area_id:areaId})},720:function(module,__webpack_exports__,__webpack_require__){"use strict";__webpack_require__.r(__webpack_exports__);var lit_element=__webpack_require__(13),paper_item=__webpack_require__(123),paper_item_body=__webpack_require__(154),paper_card=__webpack_require__(152),paper_fab=__webpack_require__(219),area_registry=__webpack_require__(369),hass_subpage=__webpack_require__(196),hass_loading_screen=__webpack_require__(139),compare=__webpack_require__(255),ha_config_section=__webpack_require__(169),fire_event=__webpack_require__(58);const loadAreaRegistryDetailDialog=()=>Promise.all([__webpack_require__.e(1),__webpack_require__.e(4),__webpack_require__.e(96),__webpack_require__.e(16)]).then(__webpack_require__.bind(null,761)),showAreaRegistryDetailDialog=(element,systemLogDetailParams)=>{Object(fire_event.a)(element,"show-dialog",{dialogTag:"dialog-area-registry-detail",dialogImport:loadAreaRegistryDetailDialog,dialogParams:systemLogDetailParams})};class ha_config_area_registry_HaConfigAreaRegistry extends lit_element.a{static get properties(){return{hass:{},isWide:{},_items:{}}}render(){if(!this.hass||this._items===void 0){return lit_element.c`
        <hass-loading-screen></hass-loading-screen>
      `}return lit_element.c`
      <hass-subpage header="Area Registry">
        <ha-config-section .isWide=${this.isWide}>
          <span slot="header">Area Registry</span>
          <span slot="introduction">
            Areas are used to organize where devices are. This information will
            be used throughout Home Assistant to help you in organizing your
            interface, permissions and integrations with other systems.
            <p>
              To place devices in an area, navigate to
              <a href="/config/integrations">the integrations page</a> and then
              click on a configured integration to get to the device cards.
            </p>
          </span>
          <paper-card>
            ${this._items.map(entry=>{return lit_element.c`
                <paper-item @click=${this._openEditEntry} .entry=${entry}>
                  <paper-item-body>
                    ${entry.name}
                  </paper-item-body>
                </paper-item>
              `})}
            ${0===this._items.length?lit_element.c`
                  <div class="empty">
                    Looks like you have no areas yet!
                    <paper-button @click=${this._createArea}>
                      CREATE AREA</paper-button
                    >
                  </div>
                `:lit_element.c``}
          </paper-card>
        </ha-config-section>
      </hass-subpage>

      <paper-fab
        ?is-wide=${this.isWide}
        icon="hass:plus"
        title="Create Area"
        @click=${this._createArea}
      ></paper-fab>
    `}firstUpdated(changedProps){super.firstUpdated(changedProps);this._fetchData();loadAreaRegistryDetailDialog()}async _fetchData(){this._items=(await Object(area_registry.c)(this.hass)).sort((ent1,ent2)=>Object(compare.a)(ent1.name,ent2.name))}_createArea(){this._openDialog()}_openEditEntry(ev){const entry=ev.currentTarget.entry;this._openDialog(entry)}_openDialog(entry){showAreaRegistryDetailDialog(this,{entry,createEntry:async values=>{const created=await Object(area_registry.a)(this.hass,values);this._items=this._items.concat(created).sort((ent1,ent2)=>Object(compare.a)(ent1.name,ent2.name))},updateEntry:async values=>{const updated=await Object(area_registry.d)(this.hass,entry.area_id,values);this._items=this._items.map(ent=>ent===entry?updated:ent)},removeEntry:async()=>{if(!confirm(`Are you sure you want to delete this area?

All devices in this area will become unassigned.`)){return!1}try{await Object(area_registry.b)(this.hass,entry.area_id);this._items=this._items.filter(ent=>ent!==entry);return!0}catch(err){return!1}}})}static get styles(){return lit_element.b`
      a {
        color: var(--primary-color);
      }
      paper-card {
        display: block;
        max-width: 600px;
        margin: 16px auto;
      }
      .empty {
        text-align: center;
      }
      paper-item {
        cursor: pointer;
        padding-top: 4px;
        padding-bottom: 4px;
      }
      paper-fab {
        position: fixed;
        bottom: 16px;
        right: 16px;
        z-index: 1;
      }

      paper-fab[is-wide] {
        bottom: 24px;
        right: 24px;
      }
    `}}customElements.define("ha-config-area-registry",ha_config_area_registry_HaConfigAreaRegistry)}}]);
//# sourceMappingURL=19da35b254bcd8f96000.chunk.js.map