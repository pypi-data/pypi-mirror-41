/*
 * Ext JS Library 3.3.1
 * Copyright(c) 2006-2010 Sencha Inc.
 * licensing@sencha.com
 * http://www.sencha.com/license
 */
Ext.grid.PropertyRecord=Ext.data.Record.create([{name:"name",type:"string"},"value"]);Ext.grid.PropertyStore=Ext.extend(Ext.util.Observable,{constructor:function(a,b){this.grid=a;this.store=new Ext.data.Store({recordType:Ext.grid.PropertyRecord});this.store.on("update",this.onUpdate,this);if(b){this.setSource(b)}Ext.grid.PropertyStore.superclass.constructor.call(this)},setSource:function(c){this.source=c;this.store.removeAll();var b=[];for(var a in c){if(this.isEditableValue(c[a])){b.push(new Ext.grid.PropertyRecord({name:a,value:c[a]},a))}}this.store.loadRecords({records:b},{},true)},onUpdate:function(e,a,d){if(d==Ext.data.Record.EDIT){var b=a.data.value;var c=a.modified.value;if(this.grid.fireEvent("beforepropertychange",this.source,a.id,b,c)!==false){this.source[a.id]=b;a.commit();this.grid.fireEvent("propertychange",this.source,a.id,b,c)}else{a.reject()}}},getProperty:function(a){return this.store.getAt(a)},isEditableValue:function(a){return Ext.isPrimitive(a)||Ext.isDate(a)},setValue:function(d,c,a){var b=this.getRec(d);if(b){b.set("value",c);this.source[d]=c}else{if(a){this.source[d]=c;b=new Ext.grid.PropertyRecord({name:d,value:c},d);this.store.add(b)}}},remove:function(b){var a=this.getRec(b);if(a){this.store.remove(a);delete this.source[b]}},getRec:function(a){return this.store.getById(a)},getSource:function(){return this.source}});Ext.grid.PropertyColumnModel=Ext.extend(Ext.grid.ColumnModel,{nameText:"Name",valueText:"Value",dateFormat:"m/j/Y",trueText:"true",falseText:"false",constructor:function(c,b){var d=Ext.grid,e=Ext.form;this.grid=c;d.PropertyColumnModel.superclass.constructor.call(this,[{header:this.nameText,width:50,sortable:true,dataIndex:"name",id:"name",menuDisabled:true},{header:this.valueText,width:50,resizable:false,dataIndex:"value",id:"value",menuDisabled:true}]);this.store=b;var a=new e.Field({autoCreate:{tag:"select",children:[{tag:"option",value:"true",html:this.trueText},{tag:"option",value:"false",html:this.falseText}]},getValue:function(){return this.el.dom.value=="true"}});this.editors={date:new d.GridEditor(new e.DateField({selectOnFocus:true})),string:new d.GridEditor(new e.TextField({selectOnFocus:true})),number:new d.GridEditor(new e.NumberField({selectOnFocus:true,style:"text-align:left;"})),"boolean":new d.GridEditor(a,{autoSize:"both"})};this.renderCellDelegate=this.renderCell.createDelegate(this);this.renderPropDelegate=this.renderProp.createDelegate(this)},renderDate:function(a){return a.dateFormat(this.dateFormat)},renderBool:function(a){return this[a?"trueText":"falseText"]},isCellEditable:function(a,b){return a==1},getRenderer:function(a){return a==1?this.renderCellDelegate:this.renderPropDelegate},renderProp:function(a){return this.getPropertyName(a)},renderCell:function(d,b,c){var a=this.grid.customRenderers[c.get("name")];if(a){return a.apply(this,arguments)}var e=d;if(Ext.isDate(d)){e=this.renderDate(d)}else{if(typeof d=="boolean"){e=this.renderBool(d)}}return Ext.util.Format.htmlEncode(e)},getPropertyName:function(b){var a=this.grid.propertyNames;return a&&a[b]?a[b]:b},getCellEditor:function(a,e){var b=this.store.getProperty(e),d=b.data.name,c=b.data.value;if(this.grid.customEditors[d]){return this.grid.customEditors[d]}if(Ext.isDate(c)){return this.editors.date}else{if(typeof c=="number"){return this.editors.number}else{if(typeof c=="boolean"){return this.editors["boolean"]}else{return this.editors.string}}}},destroy:function(){Ext.grid.PropertyColumnModel.superclass.destroy.call(this);this.destroyEditors(this.editors);this.destroyEditors(this.grid.customEditors)},destroyEditors:function(b){for(var a in b){Ext.destroy(b[a])}}});Ext.grid.PropertyGrid=Ext.extend(Ext.grid.EditorGridPanel,{enableColumnMove:false,stripeRows:false,trackMouseOver:false,clicksToEdit:1,enableHdMenu:false,viewConfig:{forceFit:true},initComponent:function(){this.customRenderers=this.customRenderers||{};this.customEditors=this.customEditors||{};this.lastEditRow=null;var b=new Ext.grid.PropertyStore(this);this.propStore=b;var a=new Ext.grid.PropertyColumnModel(this,b);b.store.sort("name","ASC");this.addEvents("beforepropertychange","propertychange");this.cm=a;this.ds=b.store;Ext.grid.PropertyGrid.superclass.initComponent.call(this);this.mon(this.selModel,"beforecellselect",function(e,d,c){if(c===0){this.startEditing.defer(200,this,[d,1]);return false}},this)},onRender:function(){Ext.grid.PropertyGrid.superclass.onRender.apply(this,arguments);this.getGridEl().addClass("x-props-grid")},afterRender:function(){Ext.grid.PropertyGrid.superclass.afterRender.apply(this,arguments);if(this.source){this.setSource(this.source)}},setSource:function(a){this.propStore.setSource(a)},getSource:function(){return this.propStore.getSource()},setProperty:function(c,b,a){this.propStore.setValue(c,b,a)},removeProperty:function(a){this.propStore.remove(a)}});Ext.reg("propertygrid",Ext.grid.PropertyGrid);