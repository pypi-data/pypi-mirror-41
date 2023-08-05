BOWERDEPS="undefined"==typeof BOWERDEPS?{}:BOWERDEPS,function(){var e,t,i,s=function(e,t){return function(){return e.apply(t,arguments)}};e=function(){function e(){return["ui.router","ui.bootstrap","ngAnimate","guanlecoja.ui","bbData"]}return e}(),i=function(){function e(e,t,i){var s,n,l;n="console",t.addGroup({name:n,caption:"Console View",icon:"exclamation-circle",order:5}),s={group:n,caption:"Console View"},l={controller:n+"Controller",controllerAs:"c",templateUrl:"console_view/views/"+n+".html",name:n,url:"/"+n,data:s},e.state(l),i.addSettingsGroup({name:"Console",caption:"Console related settings",items:[{type:"integer",name:"buildLimit",caption:"Number of builds to fetch",default_value:200},{type:"integer",name:"changeLimit",caption:"Number of changes to fetch",default_value:30}]})}return e}(),t=function(){function e(e,t,i,n,l,a,o,r){var u,h;this.$scope=e,this.$window=i,this.$uibModal=o,this.$timeout=r,this.makeFakeChange=s(this.makeFakeChange,this),this.matchBuildWithChange=s(this.matchBuildWithChange,this),this._onChange=s(this._onChange,this),this.onChange=s(this.onChange,this),angular.extend(this,a),h=l.getSettingsGroup("Console"),this.buildLimit=h.buildLimit.value,this.changeLimit=h.changeLimit.value,this.dataAccessor=n.open().closeOnDestroy(this.$scope),this._infoIsExpanded={},this.$scope.all_builders=this.all_builders=this.dataAccessor.getBuilders(),this.$scope.builders=this.builders=[],"undefined"!=typeof Intl&&null!==Intl?(u=new Intl.Collator(void 0,{numeric:!0,sensitivity:"base"}),this.strcompare=u.compare):this.strcompare=function(e,t){return t>e?-1:e===t?0:1},this.$scope.builds=this.builds=this.dataAccessor.getBuilds({property:["got_revision"],limit:this.buildLimit,order:"-started_at"}),this.changes=this.dataAccessor.getChanges({limit:this.changeLimit,order:"-changeid"}),this.buildrequests=this.dataAccessor.getBuildrequests({limit:this.buildLimit,order:"-submitted_at"}),this.buildsets=this.dataAccessor.getBuildsets({limit:this.buildLimit,order:"-submitted_at"}),this.builds.onChange=this.changes.onChange=this.buildrequests.onChange=this.buildsets.onChange=this.onChange}return e.prototype.onChange=function(e){return 0!==this.builds.length&&0!==this.all_builders.length&&this.changes.$resolved&&0!==this.buildsets.length&&0!==this.buildrequests&&null==this.onchange_debounce?this.onchange_debounce=this.$timeout(this._onChange,100):void 0},e.prototype._onChange=function(){var e,t,i,s,n,l,a,o,r,u,h,d,c,g,p;for(this.onchange_debounce=void 0,u=this.builds,s=0,a=u.length;a>s;s++)e=u[s],this.all_builders.get(e.builderid).hasBuild=!0;for(this.sortBuildersByTags(this.all_builders),null==this.changesBySSID&&(this.changesBySSID={}),null==this.changesByRevision&&(this.changesByRevision={}),h=this.changes,n=0,o=h.length;o>n;n++)i=h[n],this.changesBySSID[i.sourcestamp.ssid]=i,this.changesByRevision[i.revision]=i,this.populateChange(i);for(d=this.builds,l=0,r=d.length;r>l;l++)e=d[l],this.matchBuildWithChange(e);this.filtered_changes=[],c=this.changesBySSID,g=[];for(p in c)i=c[p],i.comments&&(i.subject=i.comments.split("\n")[0]),g.push(function(){var e,s,n,l;for(n=i.builders,l=[],s=0,e=n.length;e>s;s++){if(t=n[s],t.builds.length>0){this.filtered_changes.push(i);break}l.push(void 0)}return l}.call(this));return g},e.prototype.sortBuildersByTags=function(e){var t,i,s,n,l,a,o,r,u,h,d,c,g,p,b,f;for(s=[],i="",n=0,o=e.length;o>n;n++)t=e[n],t.hasBuild&&(s.push(t),i+="."+t.builderid);if(i!==this.last_builderids_with_builds){for(p=this._sortBuildersByTags(s),b=[],c=[],d=function(e,t,i){var s,n;if(s=b[e],null==s)s=b[e]=[];else if(n=s[s.length-1],n.tag===t)return void(n.colspan+=i);return s.push({tag:t,colspan:i})},h=this,f=function(e,t){var i,s,n,l,a,o,r;d(t,e.tag,e.builders.length);{if(null!=e.tag_line&&0!==e.tag_line.length){for(o=e.tag_line,r=[],l=0,a=o.length;a>l;l++)i=o[l],r.push(f(i,t+1));return r}for(e.builders.sort(function(e,t){return h.strcompare(e.name,t.name)}),c=c.concat(e.builders),s=n=1;100>=n;s=++n)d(t+s,"",e.builders.length)}},l=0,r=p.length;r>l;l++)g=p[l],f(g,0);for(this.builders=c,this.tag_lines=[],a=0,u=b.length;u>a;a++)p=b[a],(1!==p.length||""!==p[0].tag)&&this.tag_lines.push(p);return this.last_builderids_with_builds=i}},e.prototype._sortBuildersByTags=function(e){var t,i,s,n,l,a,o,r,u,h,d,c,g,p,b,f,m,v,_,y,w,B,C,$,S,k;for(s={},a=0,u=e.length;u>a;a++)if(t=e[a],null!=t.tags)for(y=t.tags,o=0,h=y.length;h>o;o++)$=y[o],null==s[$]&&(s[$]=[]),s[$].push(t);k=[];for($ in s)i=s[$],i.length<e.length&&k.push({tag:$,builders:i});for(k.sort(function(e,t){return t.builders.length-e.builders.length}),S=[],n={},r=0,d=k.length;d>r;r++){for($=k[r],l=!1,w=$.builders,f=0,c=w.length;c>f;f++)if(t=w[f],n.hasOwnProperty(t.builderid)){l=!0;break}if(!l){for(B=$.builders,m=0,g=B.length;g>m;m++)t=B[m],n[t.builderid]=$.tag;S.push($)}}for(C=[],v=0,p=e.length;p>v;v++)t=e[v],n.hasOwnProperty(t.builderid)||C.push(t);if(C.length&&S.push({tag:"",builders:C}),S.length>1)for(_=0,b=S.length;b>_;_++)$=S[_],$.tag_line=this._sortBuildersByTags($.builders);return S},e.prototype.populateChange=function(e){var t,i,s,n,l;for(e.builders=[],e.buildersById={},n=this.builders,l=[],i=0,s=n.length;s>i;i++)t=n[i],t={builderid:t.builderid,name:t.name,builds:[]},e.builders.push(t),l.push(e.buildersById[t.builderid]=t);return l},e.prototype.matchBuildWithChange=function(e){var t,i,s,n,l,a,o,r,u,h,d;if(t=this.buildrequests.get(e.buildrequestid),null!=t&&(i=this.buildsets.get(t.buildsetid),null!=i)){if(null!=i&&null!=i.sourcestamps)for(o=i.sourcestamps,l=0,a=o.length;a>l&&(d=o[l],s=this.changesBySSID[d.ssid],null==s);l++);if(null==s&&null!=(null!=(r=e.properties)?r.got_revision:void 0))if(u=e.properties.got_revision[0],"string"==typeof u)s=this.changesByRevision[u],null==s&&(s=this.makeFakeChange("",u,e.started_at));else{for(n in u)if(h=u[n],s=this.changesByRevision[h],null!=s)break;null==s&&(h=u==={}?"":u[u.keys()[0]],s=this.makeFakeChange(n,h,e.started_at))}return null==s&&(h="unknown revision "+e.builderid+"-"+e.buildid,s=this.makeFakeChange("unknown codebase",h,e.started_at)),s.buildersById[e.builderid].builds.push(e)}},e.prototype.makeFakeChange=function(e,t,i){var s;return s=this.changesBySSID[t],null==s&&(s={codebase:e,revision:t,changeid:t,when_timestamp:i,author:"unknown author for "+t,comments:t+"\n\nFake comment for revision: No change for this revision, please setup a changesource in Buildbot"},this.changesBySSID[t]=s,this.populateChange(s)),s},e.prototype.openAll=function(){var e,t,i,s,n;for(s=this.filtered_changes,n=[],t=0,i=s.length;i>t;t++)e=s[t],n.push(e.show_details=!0);return n},e.prototype.closeAll=function(){var e,t,i,s,n;for(s=this.filtered_changes,n=[],t=0,i=s.length;i>t;t++)e=s[t],n.push(e.show_details=!1);return n},e.prototype.getRowHeaderWidth=function(){return this.hasExpanded()?400:200},e.prototype.getColHeaderHeight=function(){var e,t,i,s,n;for(s=0,n=this.builders,t=0,i=n.length;i>t;t++)e=n[t],s=Math.max(e.name.length,s);return Math.max(100,3*s)},e.prototype.isBigTable=function(){var e;return e=this.getRowHeaderWidth(),(this.$window.innerWidth-e)/this.builders.length<40?!0:!1},e.prototype.hasExpanded=function(){var e,t,i,s;for(s=this.changes,t=0,i=s.length;i>t;t++)if(e=s[t],this.infoIsExpanded(e))return!0;return!1},e.prototype.selectBuild=function(e){var t;return t=this.$uibModal.open({templateUrl:"console_view/views/modal.html",controller:"consoleModalController as modal",windowClass:"modal-big",resolve:{selectedBuild:function(){return e}}})},e.prototype.toggleInfo=function(e){return e.show_details=!e.show_details},e.prototype.infoIsExpanded=function(e){return e.show_details},e}(),angular.module("console_view",new e).config(["$stateProvider","glMenuServiceProvider","bbSettingsServiceProvider",i]).controller("consoleController",["$scope","$q","$window","dataService","bbSettingsService","resultsService","$uibModal","$timeout",t])}.call(this),function(){var e;e=function(){function e(e,t,i){this.$uibModalInstance=t,this.selectedBuild=i,e.$on("$stateChangeStart",function(e){return function(){return e.close()}}(this))}return e.prototype.close=function(){return this.$uibModalInstance.close()},e}(),angular.module("console_view").controller("consoleModalController",["$scope","$uibModalInstance","selectedBuild",e])}.call(this),angular.module("console_view").run(["$templateCache",function(e){e.put("console_view/views/console.html",'<div class="console"><div class="load-indicator" ng-hide="c.builds.$resolved &amp;&amp; c.changes.$resolved &amp;&amp; c.buildrequests.$resolved &amp;&amp; c.buildsets.$resolved"><div class="spinner"><i class="fa fa-circle-o-notch fa-spin fa-2x"></i><p>loading</p></div></div><div ng-show="c.changes.$resolved &amp;&amp; c.filtered_changes.length==0"><p>No changes. Console view needs changesource to be setup, and<a href="#changes">changes</a>to be in the system.</p></div><table class="table table-striped table-bordered" ng-hide="c.filtered_changes.length==0" ng-class="{\'table-fixedwidth\': c.isBigTable()}"><tr class="first-row"><th class="row-header" ng-style="{\'width\': c.getRowHeaderWidth()}"><i class="fa fa-plus-circle pull-left" ng-click="c.openAll()" uib-tooltip="Open information for all changes" uib-tooltip-placement="right"></i><i class="fa fa-minus-circle pull-left" ng-click="c.closeAll()" uib-tooltip="Close information for all changes" uib-tooltip-placement="right"></i></th><th class="column" ng-repeat="builder in c.builders"><span class="builder" ng-style="{\'margin-top\': c.getColHeaderHeight()}"><a ng-href="#/builders/{{ builder.builderid }}" ng-bind="builder.name"></a></span></th></tr><tr class="tag_row" ng-repeat="tag_line in c.tag_lines"><td class="row-header"></td><td ng-repeat="tag in tag_line" colspan="{{tag.colspan}}"><span uib-tooltip="{{ tag.tag }}" ng-style="{width: tag.colspan*50}">{{tag.tag}}</span></td></tr><tr ng-repeat="change in c.filtered_changes | orderBy: [\'-when_timestamp\'] track by change.changeid"><td><changedetails change="change"></changedetails></td><td class="column" ng-repeat="builder in change.builders" title="{{builder.name}}"><a ng-repeat="build in builder.builds | orderBy: [\'number\']"><span class="badge-status" ng-if="build.buildid" ng-class="c.results2class(build, \'pulse\')" ng-click="c.selectBuild(build)">{{ build.number }}</span></a></td></tr></table></div>'),e.put("console_view/views/modal.html",'<!-- Show build summary for the selected build in a modal window--><div class="modal-header"><i class="fa fa-times pull-right" ng-click="modal.close()"></i><h4 class="modal-title">Build summary</h4></div><div class="modal-body"><buildsummary ng-if="modal.selectedBuild" buildid="modal.selectedBuild.buildid"></buildsummary></div>')}]);