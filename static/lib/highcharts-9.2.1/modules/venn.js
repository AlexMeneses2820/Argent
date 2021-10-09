/*
 Highcharts JS v9.2.1 (2021-08-19)

 (c) 2017-2021 Highsoft AS
 Authors: Jon Arild Nygard

 License: www.highcharts.com/license
*/
'use strict';(function(a){"object"===typeof module&&module.exports?(a["default"]=a,module.exports=a):"function"===typeof define&&define.amd?define("highcharts/modules/venn",["highcharts"],function(t){a(t);a.Highcharts=t;return a}):a("undefined"!==typeof Highcharts?Highcharts:void 0)})(function(a){function t(a,g,b,u){a.hasOwnProperty(g)||(a[g]=u.apply(null,b))}a=a?a._modules:{};t(a,"Core/Geometry/GeometryUtilities.js",[],function(){var a;(function(a){a.getCenterOfPoints=function(b){var a=b.reduce(function(b,
a){b.x+=a.x;b.y+=a.y;return b},{x:0,y:0});return{x:a.x/b.length,y:a.y/b.length}};a.getDistanceBetweenPoints=function(b,a){return Math.sqrt(Math.pow(a.x-b.x,2)+Math.pow(a.y-b.y,2))};a.getAngleBetweenPoints=function(b,a){return Math.atan2(a.x-b.x,a.y-b.y)}})(a||(a={}));return a});t(a,"Core/Geometry/CircleUtilities.js",[a["Core/Geometry/GeometryUtilities.js"]],function(a){var g=a.getAngleBetweenPoints,b=a.getCenterOfPoints,u=a.getDistanceBetweenPoints,p;(function(a){function q(a,f){f=Math.pow(10,f);
return Math.round(a*f)/f}function w(a){if(0>=a)throw Error("radius of circle must be a positive number.");return Math.PI*a*a}function k(a,f){return a*a*Math.acos(1-f/a)-(a-f)*Math.sqrt(f*(2*a-f))}function c(a,f){var b=u(a,f),h=a.r,n=f.r,c=[];if(b<h+n&&b>Math.abs(h-n)){h*=h;var g=(h-n*n+b*b)/(2*b);n=Math.sqrt(h-g*g);h=a.x;c=f.x;a=a.y;var k=f.y;f=h+g*(c-h)/b;g=a+g*(k-a)/b;a=n/b*-(k-a);b=n/b*-(c-h);c=[{x:q(f+a,14),y:q(g-b,14)},{x:q(f-a,14),y:q(g+b,14)}]}return c}function p(a){return a.reduce(function(a,
b,n,g){g=g.slice(n+1).reduce(function(a,f,h,g){var k=[n,h+n+1];return a.concat(c(b,f).map(function(a){a.indexes=k;return a}))},[]);return a.concat(g)},[])}function m(a,b){return u(a,b)<=b.r+1e-10}function v(a,b){return!b.some(function(b){return!m(a,b)})}function F(a){return p(a).filter(function(b){return v(b,a)})}a.round=q;a.getAreaOfCircle=w;a.getCircularSegmentArea=k;a.getOverlapBetweenCircles=function(a,b,c){var f=0;c<a+b&&(c<=Math.abs(b-a)?f=w(a<b?a:b):(f=(a*a-b*b+c*c)/(2*c),c-=f,f=k(a,a-f)+k(b,
b-c)),f=q(f,14));return f};a.getCircleCircleIntersection=c;a.getCirclesIntersectionPoints=p;a.isCircle1CompletelyOverlappingCircle2=function(a,b){return u(a,b)+b.r<a.r+1e-10};a.isPointInsideCircle=m;a.isPointInsideAllCircles=v;a.isPointOutsideAllCircles=function(a,b){return!b.some(function(b){return m(a,b)})};a.getCirclesIntersectionPolygon=F;a.getAreaOfIntersectionBetweenCircles=function(a){var f=F(a);if(1<f.length){var c=b(f);f=f.map(function(a){a.angle=g(c,a);return a}).sort(function(a,b){return b.angle-
a.angle});var h=f[f.length-1];f=f.reduce(function(f,c){var h=f.startPoint,k=b([h,c]),n=c.indexes.filter(function(a){return-1<h.indexes.indexOf(a)}).reduce(function(b,r){r=a[r];var l=g(r,c),d=g(r,h);l=d-(d-l+(d<l?2*Math.PI:0))/2;l=u(k,{x:r.x+r.r*Math.sin(l),y:r.y+r.r*Math.cos(l)});r=r.r;l>2*r&&(l=2*r);if(!b||b.width>l)b={r:r,largeArc:l>r?1:0,width:l,x:c.x,y:c.y};return b},null);if(n){var q=n.r;f.arcs.push(["A",q,q,0,n.largeArc,1,n.x,n.y]);f.startPoint=c}return f},{startPoint:h,arcs:[]}).arcs;if(0!==
f.length&&1!==f.length){f.unshift(["M",h.x,h.y]);var k={center:c,d:f}}}return k}})(p||(p={}));return p});t(a,"Mixins/NelderMead.js",[],function(){var a=function(a){a=a.slice(0,-1);for(var b=a.length,g=[],p=function(a,b){a.sum+=b[a.i];return a},m=0;m<b;m++)g[m]=a.reduce(p,{sum:0,i:m}).sum/b;return g};return{getCentroid:a,nelderMead:function(g,b){var p=function(a,b){return a.fx-b.fx},B=function(a,b,c,g){return b.map(function(b,f){return a*b+c*g[f]})},m=function(a,b){b.fx=g(b);a[a.length-1]=b;return a},
q=function(a){var b=a[0];return a.map(function(a){a=B(.5,b,.5,a);a.fx=g(a);return a})},w=function(a,b,c,k){a=B(c,a,k,b);a.fx=g(a);return a};b=function(a){var b=a.length,c=Array(b+1);c[0]=a;c[0].fx=g(a);for(var k=0;k<b;++k){var h=a.slice();h[k]=h[k]?1.05*h[k]:.001;h.fx=g(h);c[k+1]=h}return c}(b);for(var k=0;100>k;k++){b.sort(p);var c=b[b.length-1],x=a(b),y=w(x,c,2,-1);if(y.fx<b[0].fx)c=w(x,c,3,-2),b=m(b,c.fx<y.fx?c:y);else if(y.fx>=b[b.length-2].fx){var v=void 0;y.fx>c.fx?(v=w(x,c,.5,.5),b=v.fx<c.fx?
m(b,v):q(b)):(v=w(x,c,1.5,-.5),b=v.fx<y.fx?m(b,v):q(b))}else b=m(b,y)}return b[0]}}});t(a,"Mixins/DrawPoint.js",[],function(){var a=function(a){return"function"===typeof a},g=function(b){var g=this,p=b.animatableAttribs,m=b.onComplete,q=b.css,w=b.renderer,k=this.series&&this.series.chart.hasRendered?void 0:this.series&&this.series.options.animation,c=this.graphic;if(this.shouldDraw())c||(this.graphic=c=w[b.shapeType](b.shapeArgs).add(b.group)),c.css(q).attr(b.attribs).animate(p,b.isNew?!1:k,m);else if(c){var x=
function(){g.graphic=c=c&&c.destroy();a(m)&&m()};Object.keys(p).length?c.animate(p,void 0,function(){x()}):x()}};return{draw:g,drawPoint:function(a){(a.attribs=a.attribs||{})["class"]=this.getClassName();g.call(this,a)},isFn:a}});t(a,"Series/Venn/VennPoint.js",[a["Mixins/DrawPoint.js"],a["Core/Series/SeriesRegistry.js"],a["Core/Utilities.js"]],function(a,g,b){var p=this&&this.__extends||function(){var a=function(b,k){a=Object.setPrototypeOf||{__proto__:[]}instanceof Array&&function(a,b){a.__proto__=
b}||function(a,b){for(var c in b)b.hasOwnProperty(c)&&(a[c]=b[c])};return a(b,k)};return function(b,k){function c(){this.constructor=b}a(b,k);b.prototype=null===k?Object.create(k):(c.prototype=k.prototype,new c)}}(),t=b.extend,m=b.isNumber;g=function(a){function b(){var b=null!==a&&a.apply(this,arguments)||this;b.options=void 0;b.series=void 0;return b}p(b,a);b.prototype.isValid=function(){return m(this.value)};b.prototype.shouldDraw=function(){return!!this.shapeArgs};return b}(g.seriesTypes.scatter.prototype.pointClass);
t(g.prototype,{draw:a.drawPoint});return g});t(a,"Series/Venn/VennUtils.js",[a["Core/Geometry/CircleUtilities.js"],a["Core/Geometry/GeometryUtilities.js"],a["Mixins/NelderMead.js"],a["Core/Utilities.js"]],function(a,g,b,u){var p=a.getAreaOfCircle,m=a.getCircleCircleIntersection,q=a.getOverlapBetweenCircles,t=a.isPointInsideAllCircles,k=a.isPointInsideCircle,c=a.isPointOutsideAllCircles,x=g.getDistanceBetweenPoints,y=u.extend,v=u.isArray,F=u.isNumber,n=u.isObject,f=u.isString,C;(function(h){function u(a){var b=
a.filter(function(a){return 2===a.sets.length}).reduce(function(a,b){b.sets.forEach(function(d,e,l){n(a[d])||(a[d]={overlapping:{},totalOverlap:0});a[d].totalOverlap+=b.value;a[d].overlapping[l[1-e]]=b.value});return a},{});a.filter(E).forEach(function(a){y(a,b[a.sets[0]])});return a}function w(a,b,d,e,A){var c=a(b),l=a(d);A=A||100;e=e||1e-10;var r=d-b,f=1;if(b>=d)throw Error("a must be smaller than b.");if(0<c*l)throw Error("f(a) and f(b) must have opposite signs.");if(0===c)var g=b;else if(0===
l)g=d;else for(;f++<=A&&0!==k&&r>e;){r=(d-b)/2;g=b+r;var k=a(g);0<c*k?b=g:d=g}return g}function D(a,b,d){var e=a+b;return 0>=d?e:p(a<b?a:b)<=d?0:w(function(e){e=q(a,b,e);return d-e},0,e)}function C(a){var b=0;2===a.length&&(b=a[0],a=a[1],b=q(b.r,a.r,x(b,a)));return b}function E(a){return v(a.sets)&&1===a.sets.length}function z(a){var b={};return n(a)&&F(a.value)&&-1<a.value&&v(a.sets)&&0<a.sets.length&&!a.sets.some(function(a){var d=!1;!b[a]&&f(a)?b[a]=!0:d=!0;return d})}function B(a,b){return b.reduce(function(b,
e){var d=0;1<e.sets.length&&(d=e.value,e=C(e.sets.map(function(b){return a[b]})),e=d-e,d=Math.round(e*e*1E11)/1E11);return b+d},0)}function G(a,b){return b.totalOverlap-a.totalOverlap}h.geometry=g;h.geometryCircles=a;h.nelderMead=b;h.addOverlapToSets=u;h.getDistanceBetweenCirclesByOverlap=D;h.getLabelWidth=function(a,b,d){var e=b.reduce(function(a,b){return Math.min(b.r,a)},Infinity),A=d.filter(function(b){return!k(a,b)});d=function(d,e){return w(function(H){var l={x:a.x+e*H,y:a.y};l=t(l,b)&&c(l,
A);return-(d-H)+(l?0:Number.MAX_VALUE)},0,d)};return 2*Math.min(d(e,-1),d(e,1))};h.getMarginFromCircles=function(a,b,d){b=b.reduce(function(b,d){d=d.r-x(a,d);return d<=b?d:b},Number.MAX_VALUE);return b=d.reduce(function(b,d){d=x(a,d)-d.r;return d<=b?d:b},b)};h.isSet=E;h.layoutGreedyVenn=function(a){var b=[],d={};a.filter(function(a){return 1===a.sets.length}).forEach(function(a){d[a.sets[0]]=a.circle={x:Number.MAX_VALUE,y:Number.MAX_VALUE,r:Math.sqrt(a.value/Math.PI)}});var e=function(a,d){var e=
a.circle;e.x=d.x;e.y=d.y;b.push(a)};u(a);var c=a.filter(E).sort(G);e(c.shift(),{x:0,y:0});var f=a.filter(function(a){return 2===a.sets.length});c.forEach(function(a){var c=a.circle,A=c.r,H=a.overlapping,g=b.reduce(function(a,e,g){var l=e.circle,k=D(A,l.r,H[e.sets[0]]),h=[{x:l.x+k,y:l.y},{x:l.x-k,y:l.y},{x:l.x,y:l.y+k},{x:l.x,y:l.y-k}];b.slice(g+1).forEach(function(a){var b=a.circle;a=D(A,b.r,H[a.sets[0]]);h=h.concat(m({x:l.x,y:l.y,r:k},{x:b.x,y:b.y,r:a}))});h.forEach(function(b){c.x=b.x;c.y=b.y;var e=
B(d,f);e<a.loss&&(a.loss=e,a.coordinates=b)});return a},{loss:Number.MAX_VALUE,coordinates:void 0});e(a,g.coordinates)});return d};h.loss=B;h.processVennData=function(a){a=v(a)?a:[];var b=a.reduce(function(a,b){z(b)&&E(b)&&0<b.value&&-1===a.indexOf(b.sets[0])&&a.push(b.sets[0]);return a},[]).sort(),d=a.reduce(function(a,d){z(d)&&!d.sets.some(function(a){return-1===b.indexOf(a)})&&(a[d.sets.sort().join()]=d);return a},{});b.reduce(function(a,b,d,c){c.slice(d+1).forEach(function(d){a.push(b+","+d)});
return a},[]).forEach(function(a){if(!d[a]){var b={sets:a.split(","),value:0};d[a]=b}});return Object.keys(d).map(function(a){return d[a]})};h.sortByTotalOverlap=G})(C||(C={}));return C});t(a,"Series/Venn/VennSeries.js",[a["Core/Animation/AnimationUtilities.js"],a["Core/Color/Color.js"],a["Core/Geometry/CircleUtilities.js"],a["Core/Geometry/GeometryUtilities.js"],a["Mixins/NelderMead.js"],a["Core/Color/Palette.js"],a["Core/Series/SeriesRegistry.js"],a["Series/Venn/VennPoint.js"],a["Series/Venn/VennUtils.js"],
a["Core/Utilities.js"]],function(a,g,b,u,t,m,q,w,k,c){var p=this&&this.__extends||function(){var a=function(b,d){a=Object.setPrototypeOf||{__proto__:[]}instanceof Array&&function(a,b){a.__proto__=b}||function(a,b){for(var d in b)b.hasOwnProperty(d)&&(a[d]=b[d])};return a(b,d)};return function(b,d){function c(){this.constructor=b}a(b,d);b.prototype=null===d?Object.create(d):(c.prototype=d.prototype,new c)}}(),y=a.animObject,v=g.parse,F=b.getAreaOfIntersectionBetweenCircles,n=b.getCirclesIntersectionPolygon,
f=b.isCircle1CompletelyOverlappingCircle2,C=b.isPointInsideAllCircles,h=b.isPointOutsideAllCircles,B=u.getCenterOfPoints,J=t.nelderMead,D=q.seriesTypes.scatter;a=c.addEvent;var I=c.extend,E=c.isArray,z=c.isNumber,K=c.isObject,G=c.merge;c=function(a){function b(){var b=null!==a&&a.apply(this,arguments)||this;b.data=void 0;b.mapOfIdToRelation=void 0;b.options=void 0;b.points=void 0;return b}p(b,a);b.getLabelPosition=function(a,b){var d=a.reduce(function(d,c){var e=c.r/2;return[{x:c.x,y:c.y},{x:c.x+
e,y:c.y},{x:c.x-e,y:c.y},{x:c.x,y:c.y+e},{x:c.x,y:c.y-e}].reduce(function(d,c){var e=k.getMarginFromCircles(c,a,b);d.margin<e&&(d.point=c,d.margin=e);return d},d)},{point:void 0,margin:-Number.MAX_VALUE}).point;d=J(function(d){return-k.getMarginFromCircles({x:d[0],y:d[1]},a,b)},[d.x,d.y]);d={x:d[0],y:d[1]};C(d,a)&&h(d,b)||(d=1<a.length?B(n(a)):{x:a[0].x,y:a[0].y});return d};b.getLabelValues=function(a,c){var d=a.sets,e=c.reduce(function(a,b){var c=-1<d.indexOf(b.sets[0]);a[c?"internal":"external"].push(b.circle);
return a},{internal:[],external:[]});e.external=e.external.filter(function(a){return e.internal.some(function(b){return!f(a,b)})});a=b.getLabelPosition(e.internal,e.external);c=k.getLabelWidth(a,e.internal,e.external);return{position:a,width:c}};b.layout=function(a){var d={},c={};if(0<a.length){var g=k.layoutGreedyVenn(a),f=a.filter(k.isSet);a.forEach(function(a){var e=a.sets,h=e.join();if(e=k.isSet(a)?g[h]:F(e.map(function(a){return g[a]})))d[h]=e,c[h]=b.getLabelValues(a,f)})}return{mapOfIdToShape:d,
mapOfIdToLabelValues:c}};b.getScale=function(a,b,c){var d=c.bottom-c.top,e=c.right-c.left;d=Math.min(0<e?1/e*a:1,0<d?1/d*b:1);return{scale:d,centerX:a/2-(c.right+c.left)/2*d,centerY:b/2-(c.top+c.bottom)/2*d}};b.updateFieldBoundaries=function(a,b){var d=b.x-b.r,c=b.x+b.r,e=b.y+b.r;b=b.y-b.r;if(!z(a.left)||a.left>d)a.left=d;if(!z(a.right)||a.right<c)a.right=c;if(!z(a.top)||a.top>b)a.top=b;if(!z(a.bottom)||a.bottom<e)a.bottom=e;return a};b.prototype.animate=function(a){if(!a){var b=y(this.options.animation);
this.points.forEach(function(a){var d=a.shapeArgs;if(a.graphic&&d){var c={},e={};d.d?c.opacity=.001:(c.r=0,e.r=d.r);a.graphic.attr(c).animate(e,b);d.d&&setTimeout(function(){a&&a.graphic&&a.graphic.animate({opacity:1})},b.duration)}},this)}};b.prototype.drawPoints=function(){var a=this,b=a.chart,c=a.group,g=b.renderer;(a.points||[]).forEach(function(d){var e={zIndex:E(d.sets)?d.sets.length:0},f=d.shapeArgs;b.styledMode||I(e,a.pointAttribs(d,d.state));d.draw({isNew:!d.graphic,animatableAttribs:f,attribs:e,
group:c,renderer:g,shapeType:f&&f.d?"path":"circle"})})};b.prototype.init=function(){D.prototype.init.apply(this,arguments);delete this.opacity};b.prototype.pointAttribs=function(a,b){var d=this.options||{};a=G(d,{color:a&&a.color},a&&a.options||{},b&&d.states[b]||{});return{fill:v(a.color).brighten(a.brightness).get(),opacity:a.opacity,stroke:a.borderColor,"stroke-width":a.borderWidth,dashstyle:a.borderDashStyle}};b.prototype.translate=function(){var a=this.chart;this.processedXData=this.xData;this.generatePoints();
var c=k.processVennData(this.options.data);c=b.layout(c);var f=c.mapOfIdToShape,g=c.mapOfIdToLabelValues;c=Object.keys(f).filter(function(a){return(a=f[a])&&z(a.r)}).reduce(function(a,c){return b.updateFieldBoundaries(a,f[c])},{top:0,bottom:0,left:0,right:0});a=b.getScale(a.plotWidth,a.plotHeight,c);var h=a.scale,l=a.centerX,m=a.centerY;this.points.forEach(function(a){var b=E(a.sets)?a.sets:[],c=b.join(),d=f[c],e=g[c]||{};c=e.width;e=e.position;var k=a.options&&a.options.dataLabels;if(d){if(d.r)var n=
{x:l+d.x*h,y:m+d.y*h,r:d.r*h};else d.d&&(d=d.d,d.forEach(function(a){"M"===a[0]?(a[1]=l+a[1]*h,a[2]=m+a[2]*h):"A"===a[0]&&(a[1]*=h,a[2]*=h,a[6]=l+a[6]*h,a[7]=m+a[7]*h)}),n={d:d});e?(e.x=l+e.x*h,e.y=m+e.y*h):e={};z(c)&&(c=Math.round(c*h))}a.shapeArgs=n;e&&n&&(a.plotX=e.x,a.plotY=e.y);c&&n&&(a.dlOptions=G(!0,{style:{width:c}},K(k,!0)?k:void 0));a.name=a.options.name||b.join("\u2229")})};b.defaultOptions=G(D.defaultOptions,{borderColor:m.neutralColor20,borderDashStyle:"solid",borderWidth:1,brighten:0,
clip:!1,colorByPoint:!0,dataLabels:{enabled:!0,verticalAlign:"middle",formatter:function(){return this.point.name}},inactiveOtherPoints:!0,marker:!1,opacity:.75,showInLegend:!1,states:{hover:{opacity:1,borderColor:m.neutralColor80},select:{color:m.neutralColor20,borderColor:m.neutralColor100,animation:!1},inactive:{opacity:.075}},tooltip:{pointFormat:"{point.name}: {point.value}"}});return b}(D);I(c.prototype,{axisTypes:[],directTouch:!0,isCartesian:!1,pointArrayMap:["value"],pointClass:w,utils:k});
q.registerSeriesType("venn",c);"";a(c,"afterSetOptions",function(a){var b=a.options.states;this.is("venn")&&Object.keys(b).forEach(function(a){b[a].halo=!1})});return c});t(a,"masters/modules/venn.src.js",[],function(){})});
//# sourceMappingURL=venn.js.map