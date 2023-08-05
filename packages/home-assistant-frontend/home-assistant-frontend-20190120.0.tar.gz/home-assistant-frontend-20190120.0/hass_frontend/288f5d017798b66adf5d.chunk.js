(window.webpackJsonp=window.webpackJsonp||[]).push([[83],{255:function(module,__webpack_exports__,__webpack_require__){"use strict";__webpack_require__.d(__webpack_exports__,"a",function(){return addCard});__webpack_require__.d(__webpack_exports__,"f",function(){return replaceCard});__webpack_require__.d(__webpack_exports__,"c",function(){return deleteCard});__webpack_require__.d(__webpack_exports__,"h",function(){return swapCard});__webpack_require__.d(__webpack_exports__,"e",function(){return moveCard});__webpack_require__.d(__webpack_exports__,"b",function(){return addView});__webpack_require__.d(__webpack_exports__,"g",function(){return replaceView});__webpack_require__.d(__webpack_exports__,"d",function(){return deleteView});const addCard=(config,path,cardConfig)=>{const[viewIndex]=path,views=[];config.views.forEach((viewConf,index)=>{if(index!==viewIndex){views.push(config.views[index]);return}const cards=viewConf.cards?[...viewConf.cards,cardConfig]:[cardConfig];views.push(Object.assign({},viewConf,{cards}))});return Object.assign({},config,{views})},replaceCard=(config,path,cardConfig)=>{const[viewIndex,cardIndex]=path,views=[];config.views.forEach((viewConf,index)=>{if(index!==viewIndex){views.push(config.views[index]);return}views.push(Object.assign({},viewConf,{cards:(viewConf.cards||[]).map((origConf,ind)=>ind===cardIndex?cardConfig:origConf)}))});return Object.assign({},config,{views})},deleteCard=(config,path)=>{const[viewIndex,cardIndex]=path,views=[];config.views.forEach((viewConf,index)=>{if(index!==viewIndex){views.push(config.views[index]);return}views.push(Object.assign({},viewConf,{cards:(viewConf.cards||[]).filter((_origConf,ind)=>ind!==cardIndex)}))});return Object.assign({},config,{views})},swapCard=(config,path1,path2)=>{const card1=config.views[path1[0]].cards[path1[1]],card2=config.views[path2[0]].cards[path2[1]],origView1=config.views[path1[0]],newView1=Object.assign({},origView1,{cards:origView1.cards.map((origCard,index)=>index===path1[1]?card2:origCard)}),origView2=path1[0]===path2[0]?newView1:config.views[path2[0]],newView2=Object.assign({},origView2,{cards:origView2.cards.map((origCard,index)=>index===path2[1]?card1:origCard)});return Object.assign({},config,{views:config.views.map((origView,index)=>index===path2[0]?newView2:index===path1[0]?newView1:origView)})},moveCard=(config,fromPath,toPath)=>{if(fromPath[0]===toPath[0]){throw new Error("You can not move a card to the view it is in.")}const fromView=config.views[fromPath[0]],card=fromView.cards[fromPath[1]],newView1=Object.assign({},fromView,{cards:(fromView.cards||[]).filter((_origConf,ind)=>ind!==fromPath[1])}),toView=config.views[toPath[0]],cards=toView.cards?[...toView.cards,card]:[card],newView2=Object.assign({},toView,{cards});return Object.assign({},config,{views:config.views.map((origView,index)=>index===toPath[0]?newView2:index===fromPath[0]?newView1:origView)})},addView=(config,viewConfig)=>Object.assign({},config,{views:config.views.concat(viewConfig)}),replaceView=(config,viewIndex,viewConfig)=>Object.assign({},config,{views:config.views.map((origView,index)=>index===viewIndex?viewConfig:origView)}),deleteView=(config,viewIndex)=>Object.assign({},config,{views:config.views.filter((_origView,index)=>index!==viewIndex)})},705:function(module,__webpack_exports__,__webpack_require__){"use strict";__webpack_require__.r(__webpack_exports__);var lit_element=__webpack_require__(41),class_map=__webpack_require__(195),js_yaml=__webpack_require__(368),js_yaml_default=__webpack_require__.n(js_yaml),ha_style=__webpack_require__(101),paper_spinner=__webpack_require__(112),paper_dialog=__webpack_require__(181),paper_button=__webpack_require__(73),paper_dialog_scrollable=__webpack_require__(187),fire_event=__webpack_require__(66),lit_localize_mixin=__webpack_require__(155),paper_textarea=__webpack_require__(184);class hui_yaml_editor_HuiYAMLEditor extends lit_element.a{static get properties(){return{_yaml:{}}}set yaml(yaml){if(yaml===void 0){}else{this._yaml=yaml}}render(){return lit_element.c`
      ${this.renderStyle()}
      <paper-textarea
        max-rows="10"
        .value="${this._yaml}"
        @value-changed="${this._valueChanged}"
      ></paper-textarea>
    `}renderStyle(){return lit_element.c`
      <style>
        paper-textarea {
          --paper-input-container-shared-input-style_-_font-family: monospace;
        }
      </style>
    `}_valueChanged(ev){const target=ev.target;this._yaml=target.value;Object(fire_event.a)(this,"yaml-changed",{yaml:target.value})}}customElements.define("hui-yaml-editor",hui_yaml_editor_HuiYAMLEditor);var deep_clone_simple=__webpack_require__(304),create_card_element=__webpack_require__(325);const CUSTOM_TYPE_PREFIX="custom:";function getCardElementTag(type){return type.startsWith(CUSTOM_TYPE_PREFIX)?type.substr(CUSTOM_TYPE_PREFIX.length):`hui-${type}-card`}var hui_error_card=__webpack_require__(234);class hui_card_preview_HuiCardPreview extends HTMLElement{set hass(value){this._hass=value;if(this._element){this._element.hass=value}}set error(error){const configValue=Object(hui_error_card.a)(`${error.type}: ${error.message}`,void 0);this._createCard(configValue)}set config(configValue){if(!configValue){return}if(!this._element){this._createCard(configValue);return}const tag=getCardElementTag(configValue.type);if(tag.toUpperCase()===this._element.tagName){try{this._element.setConfig(Object(deep_clone_simple.a)(configValue))}catch(err){this._createCard(Object(hui_error_card.a)(err.message,configValue))}}else{this._createCard(configValue)}}_createCard(configValue){if(this._element){this.removeChild(this._element)}this._element=Object(create_card_element.a)(configValue);if(this._hass){this._element.hass=this._hass}this.appendChild(this._element)}}customElements.define("hui-card-preview",hui_card_preview_HuiCardPreview);const secretYamlType=new js_yaml_default.a.Type("!secret",{kind:"scalar",construct(data){data=data||"";return"!secret "+data}}),includeYamlType=new js_yaml_default.a.Type("!include",{kind:"scalar",construct(data){data=data||"";return"!include "+data}}),extYamlSchema=js_yaml_default.a.Schema.create([secretYamlType,includeYamlType]);var config_util=__webpack_require__(255);class hui_edit_card_HuiEditCard extends Object(lit_localize_mixin.a)(lit_element.a){static get properties(){return{hass:{},cardConfig:{},viewIndex:{},_cardIndex:{},_configElement:{},_configValue:{},_configState:{},_errorMsg:{},_uiEditor:{},_saving:{},_loading:{}}}get _dialog(){return this.shadowRoot.querySelector("paper-dialog")}get _previewEl(){return this.shadowRoot.querySelector("hui-card-preview")}constructor(){super();this._saving=!1}updated(changedProperties){super.updated(changedProperties);if(!changedProperties.has("cardConfig")){return}this._configValue={format:"yaml",value:void 0};this._configState="OK";this._uiEditor=!0;this._errorMsg=void 0;this._configElement=void 0;this._loading=!0;this._loadConfigElement(this.cardConfig)}render(){let content,preview;if(this._configElement!==void 0){if(this._uiEditor){content=lit_element.c`
          <div class="element-editor">${this._configElement}</div>
        `}else{content=lit_element.c`
          <hui-yaml-editor
            .hass="${this.hass}"
            .yaml="${this._configValue.value}"
            @yaml-changed="${this._handleYamlChanged}"
          ></hui-yaml-editor>
        `}preview=lit_element.c`
        <hr />
        <hui-card-preview .hass="${this.hass}"> </hui-card-preview>
      `}return lit_element.c`
      <paper-dialog
        with-backdrop
        opened
        @opened-changed="${this._openedChanged}"
      >
        <h2>${this.localize("ui.panel.lovelace.editor.edit_card.header")}</h2>
        <paper-spinner
          ?active="${this._loading}"
          alt="Loading"
          class="center margin-bot"
        ></paper-spinner>
        <paper-dialog-scrollable
          class="${Object(class_map.a)({hidden:this._loading})}"
        >
          ${this._errorMsg?lit_element.c`
                  <div class="error">${this._errorMsg}</div>
                `:""}
          ${content} ${preview}
        </paper-dialog-scrollable>
        ${!this._loading?lit_element.c`
                <div class="paper-dialog-buttons">
                  <paper-button
                    class="toggle-button"
                    ?hidden="${!this._configValue||!this._configValue.value}"
                    ?disabled="${null===this._configElement||"OK"!==this._configState}"
                    @click="${this._toggleEditor}"
                    >${this.localize("ui.panel.lovelace.editor.edit_card.toggle_editor")}</paper-button
                  >
                  <paper-button @click="${this.closeDialog}"
                    >${this.localize("ui.common.cancel")}</paper-button
                  >
                  <paper-button
                    ?hidden="${!this._configValue||!this._configValue.value}"
                    ?disabled="${this._saving||"OK"!==this._configState}"
                    @click="${this._save}"
                  >
                    <paper-spinner
                      ?active="${this._saving}"
                      alt="Saving"
                    ></paper-spinner>
                    ${this.localize("ui.common.save")}</paper-button
                  >
                </div>
              `:""}
      </paper-dialog>
    `}async _loadedDialog(){await this.updateComplete;this._loading=!1;this._resizeDialog()}async _resizeDialog(){await this.updateComplete;Object(fire_event.a)(this._dialog,"iron-resize")}async _save(){if(!this._isConfigValid()){alert("Your config is not valid, please fix your config before saving.");return}if(!this._isConfigChanged()){this.closeDialog();return}this._saving=!0;const cardConf="yaml"===this._configValue.format?js_yaml_default.a.safeLoad(this._configValue.value,{schema:extYamlSchema}):this._configValue.value;try{const lovelace=this.lovelace;await lovelace.saveConfig(this._creatingCard?Object(config_util.a)(lovelace.config,this.path,cardConf):Object(config_util.f)(lovelace.config,this.path,cardConf));this.closeDialog()}catch(err){alert(`Saving failed: ${err.message}`)}finally{this._saving=!1}}_handleYamlChanged(ev){this._configValue={format:"yaml",value:ev.detail.yaml};try{const config=js_yaml_default.a.safeLoad(this._configValue.value,{schema:extYamlSchema});this._updatePreview(config);this._configState="OK"}catch(err){this._configState="YAML_ERROR";this._setPreviewError({type:"YAML Error",message:err})}}_handleUIConfigChanged(value){this._configValue={format:"json",value};this._updatePreview(value)}_updatePreview(config){if(!this._previewEl){return}this._previewEl.config=config;if(this._loading){this._loadedDialog()}else{this._resizeDialog()}}_setPreviewError(error){if(!this._previewEl){return}this._previewEl.error=error;this._resizeDialog()}async _toggleEditor(){if(this._uiEditor&&"json"===this._configValue.format){this._configValue={format:"yaml",value:js_yaml_default.a.safeDump(this._configValue.value)};this._uiEditor=!this._uiEditor}else if(this._configElement&&"yaml"===this._configValue.format){const yamlConfig=this._configValue.value,cardConfig=js_yaml_default.a.safeLoad(yamlConfig,{schema:extYamlSchema});this._uiEditor=!this._uiEditor;if(cardConfig.type!==this._cardType){const succes=await this._loadConfigElement(cardConfig);if(!succes){this._loadedDialog()}this._cardType=cardConfig.type}else{this._configValue={format:"json",value:cardConfig};this._configElement.setConfig(cardConfig)}}this._resizeDialog()}_isConfigValid(){if(!this._configValue||!this._configValue.value){return!1}if("OK"===this._configState){return!0}else{return!1}}_isConfigChanged(){if(this._creatingCard){return!0}const configValue="yaml"===this._configValue.format?js_yaml_default.a.safeLoad(this._configValue.value):this._configValue.value;return JSON.stringify(configValue)!==JSON.stringify(this.cardConfig)}async _loadConfigElement(conf){if(!conf){return!1}this._errorMsg=void 0;this._loading=!0;this._configElement=void 0;const tag=getCardElementTag(conf.type),elClass=customElements.get(tag);let configElement;if(elClass&&elClass.getConfigElement){configElement=await elClass.getConfigElement()}else{this._configValue={format:"yaml",value:js_yaml_default.a.safeDump(conf)};this._uiEditor=!1;this._configElement=null;return!1}try{configElement.setConfig(conf)}catch(err){this._errorMsg=lit_element.c`
        Your config is not supported by the UI editor:<br /><b>${err.message}</b
        ><br />Falling back to YAML editor.
      `;this._configValue={format:"yaml",value:js_yaml_default.a.safeDump(conf)};this._uiEditor=!1;this._configElement=null;return!1}configElement.hass=this.hass;configElement.addEventListener("config-changed",ev=>this._handleUIConfigChanged(ev.detail.config));this._configValue={format:"json",value:conf};this._configElement=configElement;await this.updateComplete;this._updatePreview(conf);return!0}get _creatingCard(){return 1===this.path.length}_openedChanged(ev){if(!ev.detail.value){this.closeDialog()}}static get styles(){return[ha_style.b,lit_element.b`
        @media all and (max-width: 450px), all and (max-height: 500px) {
          /* overrule the ha-style-dialog max-height on small screens */
          paper-dialog {
            max-height: 100%;
            height: 100%;
          }
        }

        @media all and (min-width: 660px) {
          paper-dialog {
            width: 650px;
          }
        }

        paper-dialog {
          max-width: 650px;
        }

        .center {
          margin-left: auto;
          margin-right: auto;
        }
        .margin-bot {
          margin-bottom: 24px;
        }
        paper-button paper-spinner {
          width: 14px;
          height: 14px;
          margin-right: 20px;
        }
        paper-spinner {
          display: none;
        }
        paper-spinner[active] {
          display: block;
        }
        .hidden {
          display: none;
        }
        .element-editor {
          margin-bottom: 8px;
        }
        .error {
          color: #ef5350;
          border-bottom: 1px solid #ef5350;
        }
        hr {
          color: #000;
          opacity: 0.12;
        }
        hui-card-preview {
          padding-top: 8px;
          margin-bottom: 4px;
          display: block;
        }
        .toggle-button {
          margin-right: auto;
        }
      `]}}customElements.define("hui-edit-card",hui_edit_card_HuiEditCard);const cards=[{name:"Alarm panel",type:"alarm-panel"},{name:"Conditional",type:"conditional"},{name:"Entities",type:"entities"},{name:"Entity Button",type:"entity-button"},{name:"Entity Filter",type:"entity-filter"},{name:"Gauge",type:"gauge"},{name:"Glance",type:"glance"},{name:"History Graph",type:"history-graph"},{name:"Horizontal Stack",type:"horizontal-stack"},{name:"iFrame",type:"iframe"},{name:"Light",type:"light"},{name:"Map",type:"map"},{name:"Markdown",type:"markdown"},{name:"Media Control",type:"media-control"},{name:"Picture",type:"picture"},{name:"Picture Elements",type:"picture-elements"},{name:"Picture Entity",type:"picture-entity"},{name:"Picture Glance",type:"picture-glance"},{name:"Plant Status",type:"plant-status"},{name:"Sensor",type:"sensor"},{name:"Shopping List",type:"shopping-list"},{name:"Thermostat",type:"thermostat"},{name:"Vertical Stack",type:"vertical-stack"},{name:"Weather Forecast",type:"weather-forecast"}];class hui_card_picker_HuiCardPicker extends Object(lit_localize_mixin.a)(lit_element.a){render(){return lit_element.c`
      <h3>${this.localize("ui.panel.lovelace.editor.edit_card.pick_card")}</h3>
      <div class="cards-container">
        ${cards.map(card=>{return lit_element.c`
              <paper-button
                raised
                @click="${this._cardPicked}"
                .type="${card.type}"
                >${card.name}</paper-button
              >
            `})}
      </div>
    `}static get styles(){return[lit_element.b`
        .cards-container {
          display: flex;
          flex-wrap: wrap;
          margin-bottom: 10px;
        }
        .cards-container paper-button {
          flex: 1 0 25%;
        }
        @media all and (max-width: 450px), all and (max-height: 500px) {
          .cards-container paper-button {
            flex: 1 0 33%;
          }
        }
      `]}_cardPicked(ev){const type=ev.currentTarget.type,tag=getCardElementTag(type),elClass=customElements.get(tag);let config={type};if(elClass&&elClass.getStubConfig){const cardConfig=elClass.getStubConfig(this.hass);config=Object.assign({},config,cardConfig)}this.cardPicked(config)}}customElements.define("hui-card-picker",hui_card_picker_HuiCardPicker);class hui_dialog_pick_card_HuiDialogPickCard extends Object(lit_localize_mixin.a)(lit_element.a){static get properties(){return{}}render(){return lit_element.c`
      <paper-dialog
        with-backdrop
        opened
        @opened-changed="${this._openedChanged}"
      >
        <h2>${this.localize("ui.panel.lovelace.editor.edit_card.header")}</h2>
        <paper-dialog-scrollable>
          <hui-card-picker
            .hass="${this.hass}"
            .cardPicked="${this.cardPicked}"
          ></hui-card-picker>
        </paper-dialog-scrollable>
        <div class="paper-dialog-buttons">
          <paper-button @click="${this._skipPick}">SKIP</paper-button>
        </div>
      </paper-dialog>
    `}_openedChanged(ev){if(!ev.detail.value){this.closeDialog()}}_skipPick(){this.cardPicked({type:""})}static get styles(){return[ha_style.b,lit_element.b`
        @media all and (max-width: 450px), all and (max-height: 500px) {
          /* overrule the ha-style-dialog max-height on small screens */
          paper-dialog {
            max-height: 100%;
            height: 100%;
          }
        }

        @media all and (min-width: 660px) {
          paper-dialog {
            width: 650px;
          }
        }

        paper-dialog {
          max-width: 650px;
        }
      `]}}customElements.define("hui-dialog-pick-card",hui_dialog_pick_card_HuiDialogPickCard);__webpack_require__.d(__webpack_exports__,"HuiDialogEditCard",function(){return hui_dialog_edit_card_HuiDialogEditCard});class hui_dialog_edit_card_HuiDialogEditCard extends lit_element.a{static get properties(){return{hass:{},_params:{},_cardConfig:{}}}constructor(){super();this._cardPicked=this._cardPicked.bind(this);this._cancel=this._cancel.bind(this)}async showDialog(params){this._params=params;this._cardConfig=2===params.path.length?this._cardConfig=params.lovelace.config.views[params.path[0]].cards[params.path[1]]:void 0}render(){if(!this._params){return lit_element.c``}if(!this._cardConfig){return lit_element.c`
        <hui-dialog-pick-card
          .hass="${this.hass}"
          .cardPicked="${this._cardPicked}"
          .closeDialog="${this._cancel}"
        ></hui-dialog-pick-card>
      `}return lit_element.c`
      <hui-edit-card
        .hass="${this.hass}"
        .lovelace="${this._params.lovelace}"
        .path="${this._params.path}"
        .cardConfig="${this._cardConfig}"
        .closeDialog="${this._cancel}"
      >
      </hui-edit-card>
    `}_cardPicked(cardConf){this._cardConfig=cardConf}_cancel(){this._params=void 0;this._cardConfig=void 0}}customElements.define("hui-dialog-edit-card",hui_dialog_edit_card_HuiDialogEditCard)}}]);
//# sourceMappingURL=288f5d017798b66adf5d.chunk.js.map