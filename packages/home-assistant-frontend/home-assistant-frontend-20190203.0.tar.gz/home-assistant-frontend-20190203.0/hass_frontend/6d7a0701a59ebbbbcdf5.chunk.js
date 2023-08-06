(window.webpackJsonp=window.webpackJsonp||[]).push([[16],{156:function(module,__webpack_exports__,__webpack_require__){"use strict";__webpack_require__.d(__webpack_exports__,"a",function(){return computeDomain});function computeDomain(entityId){return entityId.substr(0,entityId.indexOf("."))}},761:function(module,__webpack_exports__,__webpack_require__){"use strict";__webpack_require__.r(__webpack_exports__);var lit_element__WEBPACK_IMPORTED_MODULE_0__=__webpack_require__(13),_polymer_paper_dialog_paper_dialog__WEBPACK_IMPORTED_MODULE_1__=__webpack_require__(178),_polymer_paper_dialog_scrollable_paper_dialog_scrollable__WEBPACK_IMPORTED_MODULE_2__=__webpack_require__(182),_polymer_paper_input_paper_input__WEBPACK_IMPORTED_MODULE_3__=__webpack_require__(78),_resources_ha_style__WEBPACK_IMPORTED_MODULE_4__=__webpack_require__(96);class DialogAreaDetail extends lit_element__WEBPACK_IMPORTED_MODULE_0__.a{static get properties(){return{_error:{},_name:{},_params:{}}}async showDialog(params){this._params=params;this._error=void 0;this._name=this._params.entry?this._params.entry.name:"";await this.updateComplete}render(){if(!this._params){return lit_element__WEBPACK_IMPORTED_MODULE_0__.c``}const nameInvalid=""===this._name.trim();return lit_element__WEBPACK_IMPORTED_MODULE_0__.c`
      <paper-dialog
        with-backdrop
        opened
        @opened-changed="${this._openedChanged}"
      >
        <h2>${this._params.entry?this._params.entry.name:"New Area"}</h2>
        <paper-dialog-scrollable>
          ${this._error?lit_element__WEBPACK_IMPORTED_MODULE_0__.c`
                <div class="error">${this._error}</div>
              `:""}
          <div class="form">
            <paper-input
              .value=${this._name}
              @value-changed=${this._nameChanged}
              label="Name"
              error-message="Name is required"
              .invalid=${nameInvalid}
            ></paper-input>
          </div>
        </paper-dialog-scrollable>
        <div class="paper-dialog-buttons">
          ${this._params.entry?lit_element__WEBPACK_IMPORTED_MODULE_0__.c`
                <paper-button
                  class="danger"
                  @click="${this._deleteEntry}"
                  .disabled=${this._submitting}
                >
                  DELETE
                </paper-button>
              `:lit_element__WEBPACK_IMPORTED_MODULE_0__.c``}
          <paper-button
            @click="${this._updateEntry}"
            .disabled=${nameInvalid||this._submitting}
          >
            ${this._params.entry?"UPDATE":"CREATE"}
          </paper-button>
        </div>
      </paper-dialog>
    `}_nameChanged(ev){this._error=void 0;this._name=ev.detail.value}async _updateEntry(){this._submitting=!0;try{const values={name:this._name.trim()};if(this._params.entry){await this._params.updateEntry(values)}else{await this._params.createEntry(values)}this._params=void 0}catch(err){this._error=err}finally{this._submitting=!1}}async _deleteEntry(){this._submitting=!0;try{if(await this._params.removeEntry()){this._params=void 0}}finally{this._submitting=!1}}_openedChanged(ev){if(!ev.detail.value){this._params=void 0}}static get styles(){return[_resources_ha_style__WEBPACK_IMPORTED_MODULE_4__.b,lit_element__WEBPACK_IMPORTED_MODULE_0__.b`
        paper-dialog {
          min-width: 400px;
        }
        .form {
          padding-bottom: 24px;
        }
        paper-button {
          font-weight: 500;
        }
        paper-button.danger {
          font-weight: 500;
          color: var(--google-red-500);
          margin-left: -12px;
          margin-right: auto;
        }
        .error {
          color: var(--google-red-500);
        }
      `]}}customElements.define("dialog-area-registry-detail",DialogAreaDetail)},764:function(module,__webpack_exports__,__webpack_require__){"use strict";__webpack_require__.r(__webpack_exports__);var lit_element__WEBPACK_IMPORTED_MODULE_0__=__webpack_require__(13),_polymer_paper_dialog_paper_dialog__WEBPACK_IMPORTED_MODULE_1__=__webpack_require__(178),_polymer_paper_dialog_scrollable_paper_dialog_scrollable__WEBPACK_IMPORTED_MODULE_2__=__webpack_require__(182),_polymer_paper_input_paper_input__WEBPACK_IMPORTED_MODULE_3__=__webpack_require__(78),_resources_ha_style__WEBPACK_IMPORTED_MODULE_4__=__webpack_require__(96),_common_entity_compute_domain__WEBPACK_IMPORTED_MODULE_5__=__webpack_require__(156),_common_entity_compute_state_name__WEBPACK_IMPORTED_MODULE_6__=__webpack_require__(103);class DialogEntityRegistryDetail extends lit_element__WEBPACK_IMPORTED_MODULE_0__.a{static get properties(){return{_error:{},_name:{},_entityId:{},_params:{}}}async showDialog(params){this._params=params;this._error=void 0;this._name=this._params.entry.name||"";this._entityId=this._params.entry.entity_id;await this.updateComplete}render(){if(!this._params){return lit_element__WEBPACK_IMPORTED_MODULE_0__.c``}const entry=this._params.entry,stateObj=this.hass.states[entry.entity_id],invalidDomainUpdate=Object(_common_entity_compute_domain__WEBPACK_IMPORTED_MODULE_5__.a)(this._entityId.trim())!==Object(_common_entity_compute_domain__WEBPACK_IMPORTED_MODULE_5__.a)(this._params.entry.entity_id);return lit_element__WEBPACK_IMPORTED_MODULE_0__.c`
      <paper-dialog
        with-backdrop
        opened
        @opened-changed="${this._openedChanged}"
      >
        <h2>${entry.entity_id}</h2>
        <paper-dialog-scrollable>
          ${!stateObj?lit_element__WEBPACK_IMPORTED_MODULE_0__.c`
                <div>This entity is not currently available.</div>
              `:""}
          ${this._error?lit_element__WEBPACK_IMPORTED_MODULE_0__.c`
                <div class="error">${this._error}</div>
              `:""}
          <div class="form">
            <paper-input
              .value=${this._name}
              @value-changed=${this._nameChanged}
              .label=${this.hass.localize("ui.dialogs.more_info_settings.name")}
              .placeholder=${stateObj?Object(_common_entity_compute_state_name__WEBPACK_IMPORTED_MODULE_6__.a)(stateObj):""}
              .disabled=${this._submitting}
            ></paper-input>
            <paper-input
              .value=${this._entityId}
              @value-changed=${this._entityIdChanged}
              .label=${this.hass.localize("ui.dialogs.more_info_settings.entity_id")}
              error-message="Domain needs to stay the same"
              .invalid=${invalidDomainUpdate}
              .disabled=${this._submitting}
            ></paper-input>
          </div>
        </paper-dialog-scrollable>
        <div class="paper-dialog-buttons">
          <paper-button
            class="danger"
            @click="${this._deleteEntry}"
            .disabled=${this._submitting}
          >
            DELETE
          </paper-button>
          <paper-button
            @click="${this._updateEntry}"
            .disabled=${invalidDomainUpdate||this._submitting}
          >
            UPDATE
          </paper-button>
        </div>
      </paper-dialog>
    `}_nameChanged(ev){this._error=void 0;this._name=ev.detail.value}_entityIdChanged(ev){this._error=void 0;this._entityId=ev.detail.value}async _updateEntry(){this._submitting=!0;try{await this._params.updateEntry({name:this._name.trim()||null,new_entity_id:this._entityId.trim()});this._params=void 0}catch(err){this._error=err}finally{this._submitting=!1}}async _deleteEntry(){this._submitting=!0;try{if(await this._params.removeEntry()){this._params=void 0}}finally{this._submitting=!1}}_openedChanged(ev){if(!ev.detail.value){this._params=void 0}}static get styles(){return[_resources_ha_style__WEBPACK_IMPORTED_MODULE_4__.b,lit_element__WEBPACK_IMPORTED_MODULE_0__.b`
        paper-dialog {
          min-width: 400px;
        }
        .form {
          padding-bottom: 24px;
        }
        paper-button {
          font-weight: 500;
        }
        paper-button.danger {
          font-weight: 500;
          color: var(--google-red-500);
          margin-left: -12px;
          margin-right: auto;
        }
        .error {
          color: var(--google-red-500);
        }
      `]}}customElements.define("dialog-entity-registry-detail",DialogEntityRegistryDetail)}}]);
//# sourceMappingURL=6d7a0701a59ebbbbcdf5.chunk.js.map