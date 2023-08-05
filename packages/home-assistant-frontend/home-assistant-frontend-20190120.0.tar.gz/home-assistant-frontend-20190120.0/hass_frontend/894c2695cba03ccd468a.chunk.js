(window.webpackJsonp=window.webpackJsonp||[]).push([[20],{186:function(module,__webpack_exports__,__webpack_require__){"use strict";__webpack_require__.d(__webpack_exports__,"a",function(){return isComponentLoaded});function isComponentLoaded(hass,component){return hass&&-1!==hass.config.components.indexOf(component)}},715:function(module,__webpack_exports__,__webpack_require__){"use strict";__webpack_require__.r(__webpack_exports__);var _polymer_app_route_app_route__WEBPACK_IMPORTED_MODULE_0__=__webpack_require__(99),_polymer_iron_media_query_iron_media_query__WEBPACK_IMPORTED_MODULE_1__=__webpack_require__(114),_polymer_polymer_lib_utils_html_tag__WEBPACK_IMPORTED_MODULE_2__=__webpack_require__(1),_polymer_polymer_polymer_element__WEBPACK_IMPORTED_MODULE_3__=__webpack_require__(11),_layouts_hass_error_screen__WEBPACK_IMPORTED_MODULE_4__=__webpack_require__(140),_common_config_is_component_loaded__WEBPACK_IMPORTED_MODULE_5__=__webpack_require__(186),_mixins_events_mixin__WEBPACK_IMPORTED_MODULE_6__=__webpack_require__(50),_mixins_navigate_mixin__WEBPACK_IMPORTED_MODULE_7__=__webpack_require__(97);Promise.all([__webpack_require__.e(0),__webpack_require__.e(1),__webpack_require__.e(2),__webpack_require__.e(3),__webpack_require__.e(50)]).then(__webpack_require__.bind(null,701));Promise.all([__webpack_require__.e(0),__webpack_require__.e(2),__webpack_require__.e(8),__webpack_require__.e(101),__webpack_require__.e(51)]).then(__webpack_require__.bind(null,702));Promise.all([__webpack_require__.e(0),__webpack_require__.e(8),__webpack_require__.e(52)]).then(__webpack_require__.bind(null,707));Promise.all([__webpack_require__.e(0),__webpack_require__.e(2),__webpack_require__.e(105),__webpack_require__.e(53)]).then(__webpack_require__.bind(null,710));Promise.all([__webpack_require__.e(0),__webpack_require__.e(2),__webpack_require__.e(4),__webpack_require__.e(5),__webpack_require__.e(54)]).then(__webpack_require__.bind(null,703));Promise.all([__webpack_require__.e(0),__webpack_require__.e(55)]).then(__webpack_require__.bind(null,711));Promise.all([__webpack_require__.e(0),__webpack_require__.e(1),__webpack_require__.e(2),__webpack_require__.e(3),__webpack_require__.e(56)]).then(__webpack_require__.bind(null,708));Promise.all([__webpack_require__.e(0),__webpack_require__.e(102),__webpack_require__.e(57)]).then(__webpack_require__.bind(null,709));Promise.all([__webpack_require__.e(0),__webpack_require__.e(5),__webpack_require__.e(58)]).then(__webpack_require__.bind(null,706));Promise.all([__webpack_require__.e(0),__webpack_require__.e(2),__webpack_require__.e(4),__webpack_require__.e(5),__webpack_require__.e(59)]).then(__webpack_require__.bind(null,704));class HaPanelConfig extends Object(_mixins_events_mixin__WEBPACK_IMPORTED_MODULE_6__.a)(Object(_mixins_navigate_mixin__WEBPACK_IMPORTED_MODULE_7__.a)(_polymer_polymer_polymer_element__WEBPACK_IMPORTED_MODULE_3__.a)){static get template(){return _polymer_polymer_lib_utils_html_tag__WEBPACK_IMPORTED_MODULE_2__.a`
      <app-route
        route="[[route]]"
        pattern="/:page"
        data="{{_routeData}}"
      ></app-route>

      <iron-media-query query="(min-width: 1040px)" query-matches="{{wide}}">
      </iron-media-query>
      <iron-media-query
        query="(min-width: 1296px)"
        query-matches="{{wideSidebar}}"
      >
      </iron-media-query>

      <template
        is="dom-if"
        if="[[_equals(_routeData.page, &quot;core&quot;)]]"
        restamp
      >
        <ha-config-core
          page-name="core"
          hass="[[hass]]"
          is-wide="[[isWide]]"
        ></ha-config-core>
      </template>

      <template
        is="dom-if"
        if="[[_equals(_routeData.page, &quot;cloud&quot;)]]"
        restamp
      >
        <ha-config-cloud
          page-name="cloud"
          route="[[route]]"
          hass="[[hass]]"
          is-wide="[[isWide]]"
          cloud-status="[[_cloudStatus]]"
        ></ha-config-cloud>
      </template>

      <template
        is="dom-if"
        if="[[_equals(_routeData.page, &quot;dashboard&quot;)]]"
      >
        <ha-config-dashboard
          page-name="dashboard"
          hass="[[hass]]"
          is-wide="[[isWide]]"
          cloud-status="[[_cloudStatus]]"
          narrow="[[narrow]]"
          show-menu="[[showMenu]]"
        ></ha-config-dashboard>
      </template>

      <template
        is="dom-if"
        if="[[_equals(_routeData.page, &quot;automation&quot;)]]"
        restamp
      >
        <ha-config-automation
          page-name="automation"
          route="[[route]]"
          hass="[[hass]]"
          is-wide="[[isWide]]"
        ></ha-config-automation>
      </template>

      <template
        is="dom-if"
        if="[[_equals(_routeData.page, &quot;script&quot;)]]"
        restamp
      >
        <ha-config-script
          page-name="script"
          route="[[route]]"
          hass="[[hass]]"
          is-wide="[[isWide]]"
        ></ha-config-script>
      </template>

      <template
        is="dom-if"
        if="[[_equals(_routeData.page, &quot;zha&quot;)]]"
        restamp
      >
        <ha-config-zha
          page-name="zha"
          hass="[[hass]]"
          is-wide="[[isWide]]"
        ></ha-config-zha>
      </template>

      <template
        is="dom-if"
        if="[[_equals(_routeData.page, &quot;zwave&quot;)]]"
        restamp
      >
        <ha-config-zwave
          page-name="zwave"
          hass="[[hass]]"
          is-wide="[[isWide]]"
        ></ha-config-zwave>
      </template>

      <template
        is="dom-if"
        if="[[_equals(_routeData.page, &quot;customize&quot;)]]"
        restamp
      >
        <ha-config-customize
          page-name="customize"
          hass="[[hass]]"
          is-wide="[[isWide]]"
        ></ha-config-customize>
      </template>

      <template
        is="dom-if"
        if="[[_equals(_routeData.page, &quot;integrations&quot;)]]"
        restamp
      >
        <ha-config-entries
          route="[[route]]"
          page-name="integrations"
          hass="[[hass]]"
          is-wide="[[isWide]]"
          narrow="[[narrow]]"
        ></ha-config-entries>
      </template>

      <template
        is="dom-if"
        if="[[_equals(_routeData.page, &quot;users&quot;)]]"
        restamp
      >
        <ha-config-users
          page-name="users"
          route="[[route]]"
          hass="[[hass]]"
        ></ha-config-users>
      </template>
    `}static get properties(){return{hass:Object,narrow:Boolean,showMenu:Boolean,_cloudStatus:{type:Object,value:null},route:{type:Object,observer:"_routeChanged"},_routeData:Object,wide:Boolean,wideSidebar:Boolean,isWide:{type:Boolean,computed:"computeIsWide(showMenu, wideSidebar, wide)"}}}ready(){super.ready();if(Object(_common_config_is_component_loaded__WEBPACK_IMPORTED_MODULE_5__.a)(this.hass,"cloud")){this._updateCloudStatus()}this.addEventListener("ha-refresh-cloud-status",()=>this._updateCloudStatus())}async _updateCloudStatus(){this._cloudStatus=await this.hass.callWS({type:"cloud/status"});if("connecting"===this._cloudStatus.cloud){setTimeout(()=>this._updateCloudStatus(),5e3)}}computeIsWide(showMenu,wideSidebar,wide){return showMenu?wideSidebar:wide}_routeChanged(route){if(""===route.path&&"/config"===route.prefix){this.navigate("/config/dashboard",!0)}this.fire("iron-resize")}_equals(a,b){return a===b}}customElements.define("ha-panel-config",HaPanelConfig)}}]);
//# sourceMappingURL=894c2695cba03ccd468a.chunk.js.map