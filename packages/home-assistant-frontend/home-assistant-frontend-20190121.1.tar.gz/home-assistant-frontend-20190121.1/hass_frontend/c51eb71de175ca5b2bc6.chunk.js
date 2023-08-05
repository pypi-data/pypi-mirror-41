(window.webpackJsonp=window.webpackJsonp||[]).push([[62],{764:function(module,__webpack_exports__,__webpack_require__){"use strict";__webpack_require__.r(__webpack_exports__);var lit_element=__webpack_require__(31),hui_entities_card=__webpack_require__(441);const EXCLUDED_DOMAINS=["zone"],computeUsedEntities=config=>{const entities=new Set,addEntityId=entity=>{if("string"===typeof entity){entities.add(entity)}else if(entity.entity){entities.add(entity.entity)}},addEntities=obj=>{if(obj.entity){addEntityId(obj.entity)}if(obj.entities){obj.entities.forEach(entity=>addEntityId(entity))}if(obj.card){addEntities(obj.card)}if(obj.cards){obj.cards.forEach(card=>addEntities(card))}if(obj.badges){obj.badges.forEach(badge=>addEntityId(badge))}};config.views.forEach(view=>addEntities(view));return entities},computeUnusedEntities=(hass,config)=>{const usedEntities=computeUsedEntities(config);return Object.keys(hass.states).filter(entity=>!usedEntities.has(entity)&&!(config.excluded_entities&&config.excluded_entities.includes(entity))&&!EXCLUDED_DOMAINS.includes(entity.split(".",1)[0])).sort()};var create_card_element=__webpack_require__(324);__webpack_require__.d(__webpack_exports__,"HuiUnusedEntities",function(){return hui_unused_entities_HuiUnusedEntities});class hui_unused_entities_HuiUnusedEntities extends lit_element.a{static get properties(){return{_hass:{},_config:{}}}set hass(hass){this._hass=hass;if(!this._element){this._createElement();return}this._element.hass=this._hass}setConfig(config){this._config=config;this._createElement()}render(){if(!this._config||!this._hass){return lit_element.c``}return lit_element.c`
      ${this.renderStyle()}
      <div id="root">${this._element}</div>
    `}renderStyle(){return lit_element.c`
      <style>
        #root {
          max-width: 600px;
          margin: 0 auto;
          padding: 8px 0;
        }
      </style>
    `}_createElement(){if(this._hass){const entities=computeUnusedEntities(this._hass,this._config).map(entity=>({entity,secondary_info:"entity-id"}));this._element=Object(create_card_element.a)({type:"entities",title:"Unused entities",entities,show_header_toggle:!1});this._element.hass=this._hass}}}customElements.define("hui-unused-entities",hui_unused_entities_HuiUnusedEntities)}}]);
//# sourceMappingURL=c51eb71de175ca5b2bc6.chunk.js.map