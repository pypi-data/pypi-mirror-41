(window.webpackJsonp=window.webpackJsonp||[]).push([[22],{124:function(module,__webpack_exports__,__webpack_require__){"use strict";var _polymer_polymer_polymer_legacy_js__WEBPACK_IMPORTED_MODULE_0__=__webpack_require__(3),_polymer_paper_styles_default_theme_js__WEBPACK_IMPORTED_MODULE_1__=__webpack_require__(40),_polymer_iron_menu_behavior_iron_menu_behavior_js__WEBPACK_IMPORTED_MODULE_2__=__webpack_require__(108),_polymer_polymer_lib_legacy_polymer_fn_js__WEBPACK_IMPORTED_MODULE_3__=__webpack_require__(4),_polymer_polymer_lib_utils_html_tag_js__WEBPACK_IMPORTED_MODULE_4__=__webpack_require__(2);/**
@license
Copyright (c) 2015 The Polymer Project Authors. All rights reserved.
This code may only be used under the BSD style license found at
http://polymer.github.io/LICENSE.txt The complete set of authors may be found at
http://polymer.github.io/AUTHORS.txt The complete set of contributors may be
found at http://polymer.github.io/CONTRIBUTORS.txt Code distributed by Google as
part of the polymer project is also subject to an additional IP rights grant
found at http://polymer.github.io/PATENTS.txt
*/Object(_polymer_polymer_lib_legacy_polymer_fn_js__WEBPACK_IMPORTED_MODULE_3__.a)({_template:_polymer_polymer_lib_utils_html_tag_js__WEBPACK_IMPORTED_MODULE_4__.a`
    <style>
      :host {
        display: block;
        padding: 8px 0;

        background: var(--paper-listbox-background-color, var(--primary-background-color));
        color: var(--paper-listbox-color, var(--primary-text-color));

        @apply --paper-listbox;
      }
    </style>

    <slot></slot>
`,is:"paper-listbox",behaviors:[_polymer_iron_menu_behavior_iron_menu_behavior_js__WEBPACK_IMPORTED_MODULE_2__.a],hostAttributes:{role:"listbox"}})},158:function(module,__webpack_exports__,__webpack_require__){"use strict";var _polymer_iron_icon_iron_icon__WEBPACK_IMPORTED_MODULE_0__=__webpack_require__(91);const IronIconClass=customElements.get("iron-icon");let loaded=!1;class HaIcon extends IronIconClass{listen(...args){super.listen(...args);if(!loaded&&"mdi"===this._iconsetName){loaded=!0;__webpack_require__.e(56).then(__webpack_require__.bind(null,211))}}}customElements.define("ha-icon",HaIcon)},163:function(module,__webpack_exports__,__webpack_require__){"use strict";var _polymer_polymer_polymer_legacy_js__WEBPACK_IMPORTED_MODULE_0__=__webpack_require__(3),_polymer_iron_flex_layout_iron_flex_layout_js__WEBPACK_IMPORTED_MODULE_1__=__webpack_require__(39),_polymer_paper_styles_typography_js__WEBPACK_IMPORTED_MODULE_2__=__webpack_require__(50),_paper_item_shared_styles_js__WEBPACK_IMPORTED_MODULE_3__=__webpack_require__(125),_polymer_polymer_lib_legacy_polymer_fn_js__WEBPACK_IMPORTED_MODULE_4__=__webpack_require__(4),_polymer_polymer_lib_utils_html_tag_js__WEBPACK_IMPORTED_MODULE_5__=__webpack_require__(2),_paper_item_behavior_js__WEBPACK_IMPORTED_MODULE_6__=__webpack_require__(105);/**
@license
Copyright (c) 2015 The Polymer Project Authors. All rights reserved.
This code may only be used under the BSD style license found at
http://polymer.github.io/LICENSE.txt The complete set of authors may be found at
http://polymer.github.io/AUTHORS.txt The complete set of contributors may be
found at http://polymer.github.io/CONTRIBUTORS.txt Code distributed by Google as
part of the polymer project is also subject to an additional IP rights grant
found at http://polymer.github.io/PATENTS.txt
*/Object(_polymer_polymer_lib_legacy_polymer_fn_js__WEBPACK_IMPORTED_MODULE_4__.a)({_template:_polymer_polymer_lib_utils_html_tag_js__WEBPACK_IMPORTED_MODULE_5__.a`
    <style include="paper-item-shared-styles"></style>
    <style>
      :host {
        @apply --layout-horizontal;
        @apply --layout-center;
        @apply --paper-font-subhead;

        @apply --paper-item;
        @apply --paper-icon-item;
      }

      .content-icon {
        @apply --layout-horizontal;
        @apply --layout-center;

        width: var(--paper-item-icon-width, 56px);
        @apply --paper-item-icon;
      }
    </style>

    <div id="contentIcon" class="content-icon">
      <slot name="item-icon"></slot>
    </div>
    <slot></slot>
`,is:"paper-icon-item",behaviors:[_paper_item_behavior_js__WEBPACK_IMPORTED_MODULE_6__.a]})},187:function(module,__webpack_exports__,__webpack_require__){"use strict";__webpack_require__.d(__webpack_exports__,"a",function(){return isComponentLoaded});function isComponentLoaded(hass,component){return hass&&-1!==hass.config.components.indexOf(component)}},188:function(module,__webpack_exports__,__webpack_require__){"use strict";__webpack_require__.d(__webpack_exports__,"a",function(){return classMap});var _lit_html_js__WEBPACK_IMPORTED_MODULE_0__=__webpack_require__(29);/**
 * @license
 * Copyright (c) 2018 The Polymer Project Authors. All rights reserved.
 * This code may only be used under the BSD style license found at
 * http://polymer.github.io/LICENSE.txt
 * The complete set of authors may be found at
 * http://polymer.github.io/AUTHORS.txt
 * The complete set of contributors may be found at
 * http://polymer.github.io/CONTRIBUTORS.txt
 * Code distributed by Google as part of the polymer project is also
 * subject to an additional IP rights grant found at
 * http://polymer.github.io/PATENTS.txt
 */if(window.navigator.userAgent.match("Trident")){DOMTokenList.prototype.toggle=function(token,force){if(force===void 0||force){this.add(token)}else{this.remove(token)}return force===void 0?!0:force}}const classMapCache=new WeakMap,classMapStatics=new WeakMap,classMap=Object(_lit_html_js__WEBPACK_IMPORTED_MODULE_0__.f)(classInfo=>part=>{if(!(part instanceof _lit_html_js__WEBPACK_IMPORTED_MODULE_0__.a)||part instanceof _lit_html_js__WEBPACK_IMPORTED_MODULE_0__.c||"class"!==part.committer.name||1<part.committer.parts.length){throw new Error("The `classMap` directive must be used in the `class` attribute "+"and must be the only part in the attribute.")}if(!classMapStatics.has(part)){part.committer.element.className=part.committer.strings.join(" ");classMapStatics.set(part,!0)}const oldInfo=classMapCache.get(part);for(const name in oldInfo){if(!(name in classInfo)){part.committer.element.classList.remove(name)}}for(const name in classInfo){if(!oldInfo||oldInfo[name]!==classInfo[name]){part.committer.element.classList.toggle(name,!!classInfo[name])}}classMapCache.set(part,classInfo)})},722:function(module,__webpack_exports__,__webpack_require__){"use strict";__webpack_require__.r(__webpack_exports__);var lit_element__WEBPACK_IMPORTED_MODULE_0__=__webpack_require__(13),lit_html_directives_class_map__WEBPACK_IMPORTED_MODULE_1__=__webpack_require__(188),_polymer_app_layout_app_toolbar_app_toolbar__WEBPACK_IMPORTED_MODULE_2__=__webpack_require__(126),_polymer_paper_icon_button_paper_icon_button__WEBPACK_IMPORTED_MODULE_3__=__webpack_require__(93),_polymer_paper_item_paper_icon_item__WEBPACK_IMPORTED_MODULE_4__=__webpack_require__(163),_polymer_paper_item_paper_item__WEBPACK_IMPORTED_MODULE_5__=__webpack_require__(123),_polymer_paper_listbox_paper_listbox__WEBPACK_IMPORTED_MODULE_6__=__webpack_require__(124),_ha_icon__WEBPACK_IMPORTED_MODULE_7__=__webpack_require__(158),_common_config_is_component_loaded__WEBPACK_IMPORTED_MODULE_8__=__webpack_require__(187),_common_dom_fire_event__WEBPACK_IMPORTED_MODULE_9__=__webpack_require__(58),_common_const__WEBPACK_IMPORTED_MODULE_10__=__webpack_require__(104);const computeInitials=name=>{if(!name){return"user"}return name.trim().split(" ").slice(0,3).map(s=>s.substr(0,1)).join("")},computeUrl=urlPath=>`/${urlPath}`,computePanels=hass=>{const panels=hass.panels,sortValue={map:1,logbook:2,history:3},result=[];Object.keys(panels).forEach(key=>{if(panels[key].title){result.push(panels[key])}});result.sort((a,b)=>{const aBuiltIn=a.component_name in sortValue,bBuiltIn=b.component_name in sortValue;if(aBuiltIn&&bBuiltIn){return sortValue[a.component_name]-sortValue[b.component_name]}if(aBuiltIn){return-1}if(bBuiltIn){return 1}if(a.title<b.title){return-1}if(a.title>b.title){return 1}return 0});return result};class HaSidebar extends lit_element__WEBPACK_IMPORTED_MODULE_0__.a{constructor(){super();this._defaultPage=localStorage.defaultPage||_common_const__WEBPACK_IMPORTED_MODULE_10__.b}render(){const hass=this.hass;if(!hass){return lit_element__WEBPACK_IMPORTED_MODULE_0__.c``}const initials=hass.user?computeInitials(hass.user.name):"";return lit_element__WEBPACK_IMPORTED_MODULE_0__.c`
      <app-toolbar>
        <div main-title>Home Assistant</div>
        ${hass.user?lit_element__WEBPACK_IMPORTED_MODULE_0__.c`
              <a
                href="/profile"
                class="${Object(lit_html_directives_class_map__WEBPACK_IMPORTED_MODULE_1__.a)({"profile-badge":!0,long:2<initials.length})}"
              >
                <paper-ripple></paper-ripple>
                ${initials}
              </a>
            `:""}
      </app-toolbar>

      <paper-listbox attr-for-selected="data-panel" .selected=${hass.panelUrl}>
        <a
          href="${computeUrl(this._defaultPage)}"
          data-panel=${this._defaultPage}
          tabindex="-1"
        >
          <paper-icon-item>
            <ha-icon slot="item-icon" icon="hass:apps"></ha-icon>
            <span class="item-text">${hass.localize("panel.states")}</span>
          </paper-icon-item>
        </a>

        ${computePanels(hass).map(panel=>lit_element__WEBPACK_IMPORTED_MODULE_0__.c`
            <a
              href="${computeUrl(panel.url_path)}"
              data-panel="${panel.url_path}"
              tabindex="-1"
            >
              <paper-icon-item>
                <ha-icon slot="item-icon" .icon="${panel.icon}"></ha-icon>
                <span class="item-text"
                  >${hass.localize(`panel.${panel.title}`)||panel.title}</span
                >
              </paper-icon-item>
            </a>
          `)}
        ${!hass.user?lit_element__WEBPACK_IMPORTED_MODULE_0__.c`
              <paper-icon-item @click=${this._handleLogOut} class="logout">
                <ha-icon slot="item-icon" icon="hass:exit-to-app"></ha-icon>
                <span class="item-text"
                  >${hass.localize("ui.sidebar.log_out")}</span
                >
              </paper-icon-item>
            `:lit_element__WEBPACK_IMPORTED_MODULE_0__.c``}
      </paper-listbox>

      <div>
        <div class="divider"></div>

        <div class="subheader">
          ${hass.localize("ui.sidebar.developer_tools")}
        </div>

        <div class="dev-tools">
          <a href="/dev-service" tabindex="-1">
            <paper-icon-button
              icon="hass:remote"
              alt="${hass.localize("panel.dev-services")}"
              title="${hass.localize("panel.dev-services")}"
            ></paper-icon-button>
          </a>
          <a href="/dev-state" tabindex="-1">
            <paper-icon-button
              icon="hass:code-tags"
              alt="${hass.localize("panel.dev-states")}"
              title="${hass.localize("panel.dev-states")}"
            ></paper-icon-button>
          </a>
          <a href="/dev-event" tabindex="-1">
            <paper-icon-button
              icon="hass:radio-tower"
              alt="${hass.localize("panel.dev-events")}"
              title="${hass.localize("panel.dev-events")}"
            ></paper-icon-button>
          </a>
          <a href="/dev-template" tabindex="-1">
            <paper-icon-button
              icon="hass:file-xml"
              alt="${hass.localize("panel.dev-templates")}"
              title="${hass.localize("panel.dev-templates")}"
            ></paper-icon-button>
          </a>
          ${Object(_common_config_is_component_loaded__WEBPACK_IMPORTED_MODULE_8__.a)(hass,"mqtt")?lit_element__WEBPACK_IMPORTED_MODULE_0__.c`
                <a href="/dev-mqtt" tabindex="-1">
                  <paper-icon-button
                    icon="hass:altimeter"
                    alt="${hass.localize("panel.dev-mqtt")}"
                    title="${hass.localize("panel.dev-mqtt")}"
                  ></paper-icon-button>
                </a>
              `:lit_element__WEBPACK_IMPORTED_MODULE_0__.c``}
          <a href="/dev-info" tabindex="-1">
            <paper-icon-button
              icon="hass:information-outline"
              alt="${hass.localize("panel.dev-info")}"
              title="${hass.localize("panel.dev-info")}"
            ></paper-icon-button>
          </a>
        </div>
      </div>
    `}static get properties(){return{hass:{},_defaultPage:{}}}shouldUpdate(changedProps){if(!this.hass||!changedProps.has("hass")){return!1}const oldHass=changedProps.get("hass");if(!oldHass){return!0}const hass=this.hass;return hass.panels!==oldHass.panels||hass.panelUrl!==oldHass.panelUrl||hass.config.components!==oldHass.config.components||hass.user!==oldHass.user||hass.localize!==oldHass.localize}_handleLogOut(){Object(_common_dom_fire_event__WEBPACK_IMPORTED_MODULE_9__.a)(this,"hass-logout")}static get styles(){return lit_element__WEBPACK_IMPORTED_MODULE_0__.b`
      :host {
        height: 100%;
        display: block;
        overflow: auto;
        -ms-user-select: none;
        -webkit-user-select: none;
        -moz-user-select: none;
        border-right: 1px solid var(--divider-color);
        background-color: var(
          --sidebar-background-color,
          var(--primary-background-color)
        );
      }

      app-toolbar {
        font-weight: 400;
        color: var(--primary-text-color);
        border-bottom: 1px solid var(--divider-color);
        background-color: var(--primary-background-color);
      }

      app-toolbar a {
        color: var(--primary-text-color);
      }

      paper-listbox {
        padding: 0;
      }

      paper-listbox > a {
        color: var(--sidebar-text-color);
        font-weight: 500;
        font-size: 14px;
        text-decoration: none;
      }

      paper-icon-item {
        margin: 8px;
        padding-left: 9px;
        border-radius: 4px;
        --paper-item-min-height: 40px;
      }

      a ha-icon {
        color: var(--sidebar-icon-color);
      }

      .iron-selected paper-icon-item:before {
        border-radius: 4px;
        position: absolute;
        top: 0;
        right: 0;
        bottom: 0;
        left: 0;
        pointer-events: none;
        content: "";
        background-color: var(--sidebar-selected-icon-color);
        opacity: 0.12;
        transition: opacity 15ms linear;
        will-change: opacity;
      }

      .iron-selected paper-icon-item[pressed]:before {
        opacity: 0.37;
      }

      paper-icon-item span {
        color: var(--sidebar-text-color);
        font-weight: 500;
        font-size: 14px;
      }

      a.iron-selected paper-icon-item ha-icon {
        color: var(--sidebar-selected-icon-color);
      }

      a.iron-selected .item-text {
        color: var(--sidebar-selected-text-color);
      }

      paper-icon-item.logout {
        margin-top: 16px;
      }

      .divider {
        height: 1px;
        background-color: var(--divider-color);
        margin: 4px 0;
      }

      .subheader {
        color: var(--sidebar-text-color);
        font-weight: 500;
        font-size: 14px;
        padding: 16px;
      }

      .dev-tools {
        display: flex;
        flex-direction: row;
        justify-content: space-between;
        padding: 0 8px;
      }

      .dev-tools a {
        color: var(--sidebar-icon-color);
      }

      .profile-badge {
        /* for ripple */
        position: relative;
        box-sizing: border-box;
        width: 40px;
        line-height: 40px;
        border-radius: 50%;
        text-align: center;
        background-color: var(--light-primary-color);
        text-decoration: none;
        color: var(--primary-text-color);
      }

      .profile-badge.long {
        font-size: 80%;
      }
    `}}customElements.define("ha-sidebar",HaSidebar)}}]);
//# sourceMappingURL=5ba69b9eda76ccab1414.chunk.js.map