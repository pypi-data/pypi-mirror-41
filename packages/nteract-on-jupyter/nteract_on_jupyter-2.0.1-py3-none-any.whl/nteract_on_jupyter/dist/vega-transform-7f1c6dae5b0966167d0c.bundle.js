(window["webpackJsonp"] = window["webpackJsonp"] || []).push([["vega-transform"],{

/***/ "../../../packages/transform-vega/src/index.tsx":
/*!**************************************************************************************************!*\
  !*** /Users/kylek/code/src/github.com/nteract/nteract-ext/packages/transform-vega/src/index.tsx ***!
  \**************************************************************************************************/
/*! exports provided: VegaEmbed, VegaLite1, Vega2, VegaLite, Vega, VegaLite2, Vega3 */
/***/ (function(module, __webpack_exports__, __webpack_require__) {

"use strict";
eval("__webpack_require__.r(__webpack_exports__);\n/* harmony export (binding) */ __webpack_require__.d(__webpack_exports__, \"VegaEmbed\", function() { return VegaEmbed; });\n/* harmony export (binding) */ __webpack_require__.d(__webpack_exports__, \"VegaLite1\", function() { return VegaLite1; });\n/* harmony export (binding) */ __webpack_require__.d(__webpack_exports__, \"Vega2\", function() { return Vega2; });\n/* harmony export (binding) */ __webpack_require__.d(__webpack_exports__, \"VegaLite\", function() { return VegaLite1; });\n/* harmony export (binding) */ __webpack_require__.d(__webpack_exports__, \"Vega\", function() { return Vega2; });\n/* harmony export (binding) */ __webpack_require__.d(__webpack_exports__, \"VegaLite2\", function() { return VegaLite2; });\n/* harmony export (binding) */ __webpack_require__.d(__webpack_exports__, \"Vega3\", function() { return Vega3; });\n/* harmony import */ var _nteract_vega_embed_v2__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! @nteract/vega-embed-v2 */ \"../../../node_modules/@nteract/vega-embed-v2/dist/index.esm.js\");\n/* harmony import */ var lodash__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(/*! lodash */ \"../../../node_modules/lodash/lodash.js\");\n/* harmony import */ var lodash__WEBPACK_IMPORTED_MODULE_1___default = /*#__PURE__*/__webpack_require__.n(lodash__WEBPACK_IMPORTED_MODULE_1__);\n/* harmony import */ var react__WEBPACK_IMPORTED_MODULE_2__ = __webpack_require__(/*! react */ \"../../../node_modules/react/index.js\");\n/* harmony import */ var react__WEBPACK_IMPORTED_MODULE_2___default = /*#__PURE__*/__webpack_require__.n(react__WEBPACK_IMPORTED_MODULE_2__);\n/* harmony import */ var vega_embed__WEBPACK_IMPORTED_MODULE_3__ = __webpack_require__(/*! vega-embed */ \"../../../node_modules/vega-embed/build/src/embed.js\");\n\n\n\n\nconst MIMETYPE_VEGA2 = \"application/vnd.vega.v2+json\";\nconst MIMETYPE_VEGA3 = \"application/vnd.vega.v3+json\";\nconst MIMETYPE_VEGALITE1 = \"application/vnd.vegalite.v1+json\";\nconst MIMETYPE_VEGALITE2 = \"application/vnd.vegalite.v2+json\";\nconst DEFAULT_WIDTH = 500;\nconst DEFAULT_HEIGHT = DEFAULT_WIDTH / 1.5;\nconst defaultCallback = () => { };\nfunction embed(el, spec, mode, version, cb) {\n    if (version === \"vega2\") {\n        const embedSpec = {\n            mode,\n            spec: Object.assign({}, spec)\n        };\n        if (mode === \"vega-lite\") {\n            embedSpec.spec.config = Object(lodash__WEBPACK_IMPORTED_MODULE_1__[\"merge\"])({\n                cell: {\n                    width: DEFAULT_WIDTH,\n                    height: DEFAULT_HEIGHT\n                }\n            }, embedSpec.spec.config);\n        }\n        Object(_nteract_vega_embed_v2__WEBPACK_IMPORTED_MODULE_0__[\"default\"])(el, embedSpec, cb);\n    }\n    else {\n        spec = Object.assign({}, spec);\n        if (mode === \"vega-lite\") {\n            spec.config = Object(lodash__WEBPACK_IMPORTED_MODULE_1__[\"merge\"])({\n                cell: {\n                    width: DEFAULT_WIDTH,\n                    height: DEFAULT_HEIGHT\n                }\n            }, spec.config);\n        }\n        Object(vega_embed__WEBPACK_IMPORTED_MODULE_3__[\"default\"])(el, spec, {\n            mode,\n            actions: false\n        })\n            .then(result => cb(null, result))\n            .catch(cb);\n    }\n}\nclass VegaEmbed extends react__WEBPACK_IMPORTED_MODULE_2__[\"Component\"] {\n    componentDidMount() {\n        if (this.el &&\n            this.props.data &&\n            this.props.embedMode &&\n            this.props.version &&\n            this.props.renderedCallback) {\n            embed(this.el, this.props.data, this.props.embedMode, this.props.version, this.props.renderedCallback);\n        }\n    }\n    shouldComponentUpdate(nextProps) {\n        return this.props.data !== nextProps.data;\n    }\n    componentDidUpdate() {\n        if (this.el &&\n            this.props.data &&\n            this.props.embedMode &&\n            this.props.version &&\n            this.props.renderedCallback) {\n            embed(this.el, this.props.data, this.props.embedMode, this.props.version, this.props.renderedCallback);\n        }\n    }\n    render() {\n        // Note: We hide vega-actions since they won't work in our environment\n        // (this is only needed for vega2, since vega-embed v3 supports hiding\n        // actions via options)\n        return (react__WEBPACK_IMPORTED_MODULE_2__[\"createElement\"](react__WEBPACK_IMPORTED_MODULE_2__[\"Fragment\"], null,\n            react__WEBPACK_IMPORTED_MODULE_2__[\"createElement\"](\"style\", null, \".vega-actions{ display: none; }\"),\n            react__WEBPACK_IMPORTED_MODULE_2__[\"createElement\"](\"div\", { ref: el => {\n                    this.el = el;\n                } })));\n    }\n}\nVegaEmbed.defaultProps = {\n    renderedCallback: defaultCallback,\n    embedMode: \"vega-lite\",\n    version: \"vega2\"\n};\nfunction VegaLite1(props) {\n    return react__WEBPACK_IMPORTED_MODULE_2__[\"createElement\"](VegaEmbed, { data: props.data, embedMode: \"vega-lite\", version: \"vega2\" });\n}\nVegaLite1.MIMETYPE = MIMETYPE_VEGALITE1;\nVegaLite1.defaultProps = {\n    mediaType: MIMETYPE_VEGA2\n};\nfunction Vega2(props) {\n    return react__WEBPACK_IMPORTED_MODULE_2__[\"createElement\"](VegaEmbed, { data: props.data, embedMode: \"vega\", version: \"vega2\" });\n}\nVega2.MIMETYPE = MIMETYPE_VEGA2;\nVega2.defaultProps = {\n    mediaType: MIMETYPE_VEGA2\n};\n// For backwards compatibility\n\nfunction VegaLite2(props) {\n    return react__WEBPACK_IMPORTED_MODULE_2__[\"createElement\"](VegaEmbed, { data: props.data, embedMode: \"vega-lite\", version: \"vega3\" });\n}\nVegaLite2.MIMETYPE = MIMETYPE_VEGALITE2;\nVegaLite2.defaultProps = {\n    mediaType: MIMETYPE_VEGALITE2\n};\nfunction Vega3(props) {\n    return react__WEBPACK_IMPORTED_MODULE_2__[\"createElement\"](VegaEmbed, { data: props.data, embedMode: \"vega\", version: \"vega3\" });\n}\nVega3.MIMETYPE = MIMETYPE_VEGA3;\nVega3.defaultProps = {\n    mediaType: MIMETYPE_VEGA3\n};\n//# sourceURL=[module]\n//# sourceMappingURL=data:application/json;charset=utf-8;base64,eyJ2ZXJzaW9uIjozLCJmaWxlIjoiLi4vLi4vLi4vcGFja2FnZXMvdHJhbnNmb3JtLXZlZ2Evc3JjL2luZGV4LnRzeC5qcyIsInNvdXJjZXMiOlsid2VicGFjazovLy8vVXNlcnMva3lsZWsvY29kZS9zcmMvZ2l0aHViLmNvbS9udGVyYWN0L250ZXJhY3QtZXh0L3BhY2thZ2VzL3RyYW5zZm9ybS12ZWdhL3NyYy9pbmRleC50c3g/MmFhOCJdLCJzb3VyY2VzQ29udGVudCI6WyJpbXBvcnQgdmVnYUVtYmVkMiBmcm9tIFwiQG50ZXJhY3QvdmVnYS1lbWJlZC12MlwiO1xuaW1wb3J0IHsgbWVyZ2UgfSBmcm9tIFwibG9kYXNoXCI7XG5pbXBvcnQgKiBhcyBSZWFjdCBmcm9tIFwicmVhY3RcIjtcbmltcG9ydCB2ZWdhRW1iZWQzIGZyb20gXCJ2ZWdhLWVtYmVkXCI7XG5jb25zdCBNSU1FVFlQRV9WRUdBMiA9IFwiYXBwbGljYXRpb24vdm5kLnZlZ2EudjIranNvblwiO1xuY29uc3QgTUlNRVRZUEVfVkVHQTMgPSBcImFwcGxpY2F0aW9uL3ZuZC52ZWdhLnYzK2pzb25cIjtcbmNvbnN0IE1JTUVUWVBFX1ZFR0FMSVRFMSA9IFwiYXBwbGljYXRpb24vdm5kLnZlZ2FsaXRlLnYxK2pzb25cIjtcbmNvbnN0IE1JTUVUWVBFX1ZFR0FMSVRFMiA9IFwiYXBwbGljYXRpb24vdm5kLnZlZ2FsaXRlLnYyK2pzb25cIjtcbmNvbnN0IERFRkFVTFRfV0lEVEggPSA1MDA7XG5jb25zdCBERUZBVUxUX0hFSUdIVCA9IERFRkFVTFRfV0lEVEggLyAxLjU7XG5jb25zdCBkZWZhdWx0Q2FsbGJhY2sgPSAoKSA9PiB7IH07XG5mdW5jdGlvbiBlbWJlZChlbCwgc3BlYywgbW9kZSwgdmVyc2lvbiwgY2IpIHtcbiAgICBpZiAodmVyc2lvbiA9PT0gXCJ2ZWdhMlwiKSB7XG4gICAgICAgIGNvbnN0IGVtYmVkU3BlYyA9IHtcbiAgICAgICAgICAgIG1vZGUsXG4gICAgICAgICAgICBzcGVjOiBPYmplY3QuYXNzaWduKHt9LCBzcGVjKVxuICAgICAgICB9O1xuICAgICAgICBpZiAobW9kZSA9PT0gXCJ2ZWdhLWxpdGVcIikge1xuICAgICAgICAgICAgZW1iZWRTcGVjLnNwZWMuY29uZmlnID0gbWVyZ2Uoe1xuICAgICAgICAgICAgICAgIGNlbGw6IHtcbiAgICAgICAgICAgICAgICAgICAgd2lkdGg6IERFRkFVTFRfV0lEVEgsXG4gICAgICAgICAgICAgICAgICAgIGhlaWdodDogREVGQVVMVF9IRUlHSFRcbiAgICAgICAgICAgICAgICB9XG4gICAgICAgICAgICB9LCBlbWJlZFNwZWMuc3BlYy5jb25maWcpO1xuICAgICAgICB9XG4gICAgICAgIHZlZ2FFbWJlZDIoZWwsIGVtYmVkU3BlYywgY2IpO1xuICAgIH1cbiAgICBlbHNlIHtcbiAgICAgICAgc3BlYyA9IE9iamVjdC5hc3NpZ24oe30sIHNwZWMpO1xuICAgICAgICBpZiAobW9kZSA9PT0gXCJ2ZWdhLWxpdGVcIikge1xuICAgICAgICAgICAgc3BlYy5jb25maWcgPSBtZXJnZSh7XG4gICAgICAgICAgICAgICAgY2VsbDoge1xuICAgICAgICAgICAgICAgICAgICB3aWR0aDogREVGQVVMVF9XSURUSCxcbiAgICAgICAgICAgICAgICAgICAgaGVpZ2h0OiBERUZBVUxUX0hFSUdIVFxuICAgICAgICAgICAgICAgIH1cbiAgICAgICAgICAgIH0sIHNwZWMuY29uZmlnKTtcbiAgICAgICAgfVxuICAgICAgICB2ZWdhRW1iZWQzKGVsLCBzcGVjLCB7XG4gICAgICAgICAgICBtb2RlLFxuICAgICAgICAgICAgYWN0aW9uczogZmFsc2VcbiAgICAgICAgfSlcbiAgICAgICAgICAgIC50aGVuKHJlc3VsdCA9PiBjYihudWxsLCByZXN1bHQpKVxuICAgICAgICAgICAgLmNhdGNoKGNiKTtcbiAgICB9XG59XG5leHBvcnQgY2xhc3MgVmVnYUVtYmVkIGV4dGVuZHMgUmVhY3QuQ29tcG9uZW50IHtcbiAgICBjb21wb25lbnREaWRNb3VudCgpIHtcbiAgICAgICAgaWYgKHRoaXMuZWwgJiZcbiAgICAgICAgICAgIHRoaXMucHJvcHMuZGF0YSAmJlxuICAgICAgICAgICAgdGhpcy5wcm9wcy5lbWJlZE1vZGUgJiZcbiAgICAgICAgICAgIHRoaXMucHJvcHMudmVyc2lvbiAmJlxuICAgICAgICAgICAgdGhpcy5wcm9wcy5yZW5kZXJlZENhbGxiYWNrKSB7XG4gICAgICAgICAgICBlbWJlZCh0aGlzLmVsLCB0aGlzLnByb3BzLmRhdGEsIHRoaXMucHJvcHMuZW1iZWRNb2RlLCB0aGlzLnByb3BzLnZlcnNpb24sIHRoaXMucHJvcHMucmVuZGVyZWRDYWxsYmFjayk7XG4gICAgICAgIH1cbiAgICB9XG4gICAgc2hvdWxkQ29tcG9uZW50VXBkYXRlKG5leHRQcm9wcykge1xuICAgICAgICByZXR1cm4gdGhpcy5wcm9wcy5kYXRhICE9PSBuZXh0UHJvcHMuZGF0YTtcbiAgICB9XG4gICAgY29tcG9uZW50RGlkVXBkYXRlKCkge1xuICAgICAgICBpZiAodGhpcy5lbCAmJlxuICAgICAgICAgICAgdGhpcy5wcm9wcy5kYXRhICYmXG4gICAgICAgICAgICB0aGlzLnByb3BzLmVtYmVkTW9kZSAmJlxuICAgICAgICAgICAgdGhpcy5wcm9wcy52ZXJzaW9uICYmXG4gICAgICAgICAgICB0aGlzLnByb3BzLnJlbmRlcmVkQ2FsbGJhY2spIHtcbiAgICAgICAgICAgIGVtYmVkKHRoaXMuZWwsIHRoaXMucHJvcHMuZGF0YSwgdGhpcy5wcm9wcy5lbWJlZE1vZGUsIHRoaXMucHJvcHMudmVyc2lvbiwgdGhpcy5wcm9wcy5yZW5kZXJlZENhbGxiYWNrKTtcbiAgICAgICAgfVxuICAgIH1cbiAgICByZW5kZXIoKSB7XG4gICAgICAgIC8vIE5vdGU6IFdlIGhpZGUgdmVnYS1hY3Rpb25zIHNpbmNlIHRoZXkgd29uJ3Qgd29yayBpbiBvdXIgZW52aXJvbm1lbnRcbiAgICAgICAgLy8gKHRoaXMgaXMgb25seSBuZWVkZWQgZm9yIHZlZ2EyLCBzaW5jZSB2ZWdhLWVtYmVkIHYzIHN1cHBvcnRzIGhpZGluZ1xuICAgICAgICAvLyBhY3Rpb25zIHZpYSBvcHRpb25zKVxuICAgICAgICByZXR1cm4gKFJlYWN0LmNyZWF0ZUVsZW1lbnQoUmVhY3QuRnJhZ21lbnQsIG51bGwsXG4gICAgICAgICAgICBSZWFjdC5jcmVhdGVFbGVtZW50KFwic3R5bGVcIiwgbnVsbCwgXCIudmVnYS1hY3Rpb25zeyBkaXNwbGF5OiBub25lOyB9XCIpLFxuICAgICAgICAgICAgUmVhY3QuY3JlYXRlRWxlbWVudChcImRpdlwiLCB7IHJlZjogZWwgPT4ge1xuICAgICAgICAgICAgICAgICAgICB0aGlzLmVsID0gZWw7XG4gICAgICAgICAgICAgICAgfSB9KSkpO1xuICAgIH1cbn1cblZlZ2FFbWJlZC5kZWZhdWx0UHJvcHMgPSB7XG4gICAgcmVuZGVyZWRDYWxsYmFjazogZGVmYXVsdENhbGxiYWNrLFxuICAgIGVtYmVkTW9kZTogXCJ2ZWdhLWxpdGVcIixcbiAgICB2ZXJzaW9uOiBcInZlZ2EyXCJcbn07XG5leHBvcnQgZnVuY3Rpb24gVmVnYUxpdGUxKHByb3BzKSB7XG4gICAgcmV0dXJuIFJlYWN0LmNyZWF0ZUVsZW1lbnQoVmVnYUVtYmVkLCB7IGRhdGE6IHByb3BzLmRhdGEsIGVtYmVkTW9kZTogXCJ2ZWdhLWxpdGVcIiwgdmVyc2lvbjogXCJ2ZWdhMlwiIH0pO1xufVxuVmVnYUxpdGUxLk1JTUVUWVBFID0gTUlNRVRZUEVfVkVHQUxJVEUxO1xuVmVnYUxpdGUxLmRlZmF1bHRQcm9wcyA9IHtcbiAgICBtZWRpYVR5cGU6IE1JTUVUWVBFX1ZFR0EyXG59O1xuZXhwb3J0IGZ1bmN0aW9uIFZlZ2EyKHByb3BzKSB7XG4gICAgcmV0dXJuIFJlYWN0LmNyZWF0ZUVsZW1lbnQoVmVnYUVtYmVkLCB7IGRhdGE6IHByb3BzLmRhdGEsIGVtYmVkTW9kZTogXCJ2ZWdhXCIsIHZlcnNpb246IFwidmVnYTJcIiB9KTtcbn1cblZlZ2EyLk1JTUVUWVBFID0gTUlNRVRZUEVfVkVHQTI7XG5WZWdhMi5kZWZhdWx0UHJvcHMgPSB7XG4gICAgbWVkaWFUeXBlOiBNSU1FVFlQRV9WRUdBMlxufTtcbi8vIEZvciBiYWNrd2FyZHMgY29tcGF0aWJpbGl0eVxuZXhwb3J0IHsgVmVnYUxpdGUxIGFzIFZlZ2FMaXRlLCBWZWdhMiBhcyBWZWdhIH07XG5leHBvcnQgZnVuY3Rpb24gVmVnYUxpdGUyKHByb3BzKSB7XG4gICAgcmV0dXJuIFJlYWN0LmNyZWF0ZUVsZW1lbnQoVmVnYUVtYmVkLCB7IGRhdGE6IHByb3BzLmRhdGEsIGVtYmVkTW9kZTogXCJ2ZWdhLWxpdGVcIiwgdmVyc2lvbjogXCJ2ZWdhM1wiIH0pO1xufVxuVmVnYUxpdGUyLk1JTUVUWVBFID0gTUlNRVRZUEVfVkVHQUxJVEUyO1xuVmVnYUxpdGUyLmRlZmF1bHRQcm9wcyA9IHtcbiAgICBtZWRpYVR5cGU6IE1JTUVUWVBFX1ZFR0FMSVRFMlxufTtcbmV4cG9ydCBmdW5jdGlvbiBWZWdhMyhwcm9wcykge1xuICAgIHJldHVybiBSZWFjdC5jcmVhdGVFbGVtZW50KFZlZ2FFbWJlZCwgeyBkYXRhOiBwcm9wcy5kYXRhLCBlbWJlZE1vZGU6IFwidmVnYVwiLCB2ZXJzaW9uOiBcInZlZ2EzXCIgfSk7XG59XG5WZWdhMy5NSU1FVFlQRSA9IE1JTUVUWVBFX1ZFR0EzO1xuVmVnYTMuZGVmYXVsdFByb3BzID0ge1xuICAgIG1lZGlhVHlwZTogTUlNRVRZUEVfVkVHQTNcbn07XG4iXSwibWFwcGluZ3MiOiJBQUFBO0FBQUE7QUFBQTtBQUFBO0FBQUE7QUFBQTtBQUFBO0FBQUE7QUFBQTtBQUFBO0FBQUE7QUFBQTtBQUFBO0FBQUE7QUFBQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBOyIsInNvdXJjZVJvb3QiOiIifQ==\n//# sourceURL=webpack-internal:///../../../packages/transform-vega/src/index.tsx\n");

/***/ }),

/***/ 0:
/*!*********************!*\
  !*** url (ignored) ***!
  \*********************/
/*! no static exports found */
/***/ (function(module, exports) {

/* (ignored) */

/***/ }),

/***/ 1:
/*!********************!*\
  !*** fs (ignored) ***!
  \********************/
/*! no static exports found */
/***/ (function(module, exports) {

/* (ignored) */

/***/ }),

/***/ 2:
/*!******************************!*\
  !*** sync-request (ignored) ***!
  \******************************/
/*! no static exports found */
/***/ (function(module, exports) {

/* (ignored) */

/***/ }),

/***/ 3:
/*!*************************!*\
  !*** request (ignored) ***!
  \*************************/
/*! no static exports found */
/***/ (function(module, exports) {

/* (ignored) */

/***/ }),

/***/ 4:
/*!****************************!*\
  !*** node-fetch (ignored) ***!
  \****************************/
/*! no static exports found */
/***/ (function(module, exports) {

/* (ignored) */

/***/ }),

/***/ 5:
/*!********************!*\
  !*** fs (ignored) ***!
  \********************/
/*! no static exports found */
/***/ (function(module, exports) {

/* (ignored) */

/***/ })

}]);