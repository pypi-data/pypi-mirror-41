/******/ (function(modules) { // webpackBootstrap
/******/ 	// install a JSONP callback for chunk loading
/******/ 	function webpackJsonpCallback(data) {
/******/ 		var chunkIds = data[0];
/******/ 		var moreModules = data[1];
/******/ 		var executeModules = data[2];
/******/
/******/ 		// add "moreModules" to the modules object,
/******/ 		// then flag all "chunkIds" as loaded and fire callback
/******/ 		var moduleId, chunkId, i = 0, resolves = [];
/******/ 		for(;i < chunkIds.length; i++) {
/******/ 			chunkId = chunkIds[i];
/******/ 			if(installedChunks[chunkId]) {
/******/ 				resolves.push(installedChunks[chunkId][0]);
/******/ 			}
/******/ 			installedChunks[chunkId] = 0;
/******/ 		}
/******/ 		for(moduleId in moreModules) {
/******/ 			if(Object.prototype.hasOwnProperty.call(moreModules, moduleId)) {
/******/ 				modules[moduleId] = moreModules[moduleId];
/******/ 			}
/******/ 		}
/******/ 		if(parentJsonpFunction) parentJsonpFunction(data);
/******/
/******/ 		while(resolves.length) {
/******/ 			resolves.shift()();
/******/ 		}
/******/
/******/ 		// add entry modules from loaded chunk to deferred list
/******/ 		deferredModules.push.apply(deferredModules, executeModules || []);
/******/
/******/ 		// run deferred modules when all chunks ready
/******/ 		return checkDeferredModules();
/******/ 	};
/******/ 	function checkDeferredModules() {
/******/ 		var result;
/******/ 		for(var i = 0; i < deferredModules.length; i++) {
/******/ 			var deferredModule = deferredModules[i];
/******/ 			var fulfilled = true;
/******/ 			for(var j = 1; j < deferredModule.length; j++) {
/******/ 				var depId = deferredModule[j];
/******/ 				if(installedChunks[depId] !== 0) fulfilled = false;
/******/ 			}
/******/ 			if(fulfilled) {
/******/ 				deferredModules.splice(i--, 1);
/******/ 				result = __webpack_require__(__webpack_require__.s = deferredModule[0]);
/******/ 			}
/******/ 		}
/******/ 		return result;
/******/ 	}
/******/ 	function hotDisposeChunk(chunkId) {
/******/ 		delete installedChunks[chunkId];
/******/ 	}
/******/ 	var parentHotUpdateCallback = window["webpackHotUpdate"];
/******/ 	window["webpackHotUpdate"] = // eslint-disable-next-line no-unused-vars
/******/ 	function webpackHotUpdateCallback(chunkId, moreModules) {
/******/ 		hotAddUpdateChunk(chunkId, moreModules);
/******/ 		if (parentHotUpdateCallback) parentHotUpdateCallback(chunkId, moreModules);
/******/ 	} ;
/******/
/******/ 	// eslint-disable-next-line no-unused-vars
/******/ 	function hotDownloadUpdateChunk(chunkId) {
/******/ 		var head = document.getElementsByTagName("head")[0];
/******/ 		var script = document.createElement("script");
/******/ 		script.charset = "utf-8";
/******/ 		script.src = __webpack_require__.p + "" + chunkId + "." + hotCurrentHash + ".hot-update.js";
/******/ 		if (null) script.crossOrigin = null;
/******/ 		head.appendChild(script);
/******/ 	}
/******/
/******/ 	// eslint-disable-next-line no-unused-vars
/******/ 	function hotDownloadManifest(requestTimeout) {
/******/ 		requestTimeout = requestTimeout || 10000;
/******/ 		return new Promise(function(resolve, reject) {
/******/ 			if (typeof XMLHttpRequest === "undefined") {
/******/ 				return reject(new Error("No browser support"));
/******/ 			}
/******/ 			try {
/******/ 				var request = new XMLHttpRequest();
/******/ 				var requestPath = __webpack_require__.p + "" + hotCurrentHash + ".hot-update.json";
/******/ 				request.open("GET", requestPath, true);
/******/ 				request.timeout = requestTimeout;
/******/ 				request.send(null);
/******/ 			} catch (err) {
/******/ 				return reject(err);
/******/ 			}
/******/ 			request.onreadystatechange = function() {
/******/ 				if (request.readyState !== 4) return;
/******/ 				if (request.status === 0) {
/******/ 					// timeout
/******/ 					reject(
/******/ 						new Error("Manifest request to " + requestPath + " timed out.")
/******/ 					);
/******/ 				} else if (request.status === 404) {
/******/ 					// no update available
/******/ 					resolve();
/******/ 				} else if (request.status !== 200 && request.status !== 304) {
/******/ 					// other failure
/******/ 					reject(new Error("Manifest request to " + requestPath + " failed."));
/******/ 				} else {
/******/ 					// success
/******/ 					try {
/******/ 						var update = JSON.parse(request.responseText);
/******/ 					} catch (e) {
/******/ 						reject(e);
/******/ 						return;
/******/ 					}
/******/ 					resolve(update);
/******/ 				}
/******/ 			};
/******/ 		});
/******/ 	}
/******/
/******/ 	var hotApplyOnUpdate = true;
/******/ 	// eslint-disable-next-line no-unused-vars
/******/ 	var hotCurrentHash = "be151f1552fcded7cdb4";
/******/ 	var hotRequestTimeout = 10000;
/******/ 	var hotCurrentModuleData = {};
/******/ 	var hotCurrentChildModule;
/******/ 	// eslint-disable-next-line no-unused-vars
/******/ 	var hotCurrentParents = [];
/******/ 	// eslint-disable-next-line no-unused-vars
/******/ 	var hotCurrentParentsTemp = [];
/******/
/******/ 	// eslint-disable-next-line no-unused-vars
/******/ 	function hotCreateRequire(moduleId) {
/******/ 		var me = installedModules[moduleId];
/******/ 		if (!me) return __webpack_require__;
/******/ 		var fn = function(request) {
/******/ 			if (me.hot.active) {
/******/ 				if (installedModules[request]) {
/******/ 					if (installedModules[request].parents.indexOf(moduleId) === -1) {
/******/ 						installedModules[request].parents.push(moduleId);
/******/ 					}
/******/ 				} else {
/******/ 					hotCurrentParents = [moduleId];
/******/ 					hotCurrentChildModule = request;
/******/ 				}
/******/ 				if (me.children.indexOf(request) === -1) {
/******/ 					me.children.push(request);
/******/ 				}
/******/ 			} else {
/******/ 				console.warn(
/******/ 					"[HMR] unexpected require(" +
/******/ 						request +
/******/ 						") from disposed module " +
/******/ 						moduleId
/******/ 				);
/******/ 				hotCurrentParents = [];
/******/ 			}
/******/ 			return __webpack_require__(request);
/******/ 		};
/******/ 		var ObjectFactory = function ObjectFactory(name) {
/******/ 			return {
/******/ 				configurable: true,
/******/ 				enumerable: true,
/******/ 				get: function() {
/******/ 					return __webpack_require__[name];
/******/ 				},
/******/ 				set: function(value) {
/******/ 					__webpack_require__[name] = value;
/******/ 				}
/******/ 			};
/******/ 		};
/******/ 		for (var name in __webpack_require__) {
/******/ 			if (
/******/ 				Object.prototype.hasOwnProperty.call(__webpack_require__, name) &&
/******/ 				name !== "e" &&
/******/ 				name !== "t"
/******/ 			) {
/******/ 				Object.defineProperty(fn, name, ObjectFactory(name));
/******/ 			}
/******/ 		}
/******/ 		fn.e = function(chunkId) {
/******/ 			if (hotStatus === "ready") hotSetStatus("prepare");
/******/ 			hotChunksLoading++;
/******/ 			return __webpack_require__.e(chunkId).then(finishChunkLoading, function(err) {
/******/ 				finishChunkLoading();
/******/ 				throw err;
/******/ 			});
/******/
/******/ 			function finishChunkLoading() {
/******/ 				hotChunksLoading--;
/******/ 				if (hotStatus === "prepare") {
/******/ 					if (!hotWaitingFilesMap[chunkId]) {
/******/ 						hotEnsureUpdateChunk(chunkId);
/******/ 					}
/******/ 					if (hotChunksLoading === 0 && hotWaitingFiles === 0) {
/******/ 						hotUpdateDownloaded();
/******/ 					}
/******/ 				}
/******/ 			}
/******/ 		};
/******/ 		fn.t = function(value, mode) {
/******/ 			if (mode & 1) value = fn(value);
/******/ 			return __webpack_require__.t(value, mode & ~1);
/******/ 		};
/******/ 		return fn;
/******/ 	}
/******/
/******/ 	// eslint-disable-next-line no-unused-vars
/******/ 	function hotCreateModule(moduleId) {
/******/ 		var hot = {
/******/ 			// private stuff
/******/ 			_acceptedDependencies: {},
/******/ 			_declinedDependencies: {},
/******/ 			_selfAccepted: false,
/******/ 			_selfDeclined: false,
/******/ 			_disposeHandlers: [],
/******/ 			_main: hotCurrentChildModule !== moduleId,
/******/
/******/ 			// Module API
/******/ 			active: true,
/******/ 			accept: function(dep, callback) {
/******/ 				if (dep === undefined) hot._selfAccepted = true;
/******/ 				else if (typeof dep === "function") hot._selfAccepted = dep;
/******/ 				else if (typeof dep === "object")
/******/ 					for (var i = 0; i < dep.length; i++)
/******/ 						hot._acceptedDependencies[dep[i]] = callback || function() {};
/******/ 				else hot._acceptedDependencies[dep] = callback || function() {};
/******/ 			},
/******/ 			decline: function(dep) {
/******/ 				if (dep === undefined) hot._selfDeclined = true;
/******/ 				else if (typeof dep === "object")
/******/ 					for (var i = 0; i < dep.length; i++)
/******/ 						hot._declinedDependencies[dep[i]] = true;
/******/ 				else hot._declinedDependencies[dep] = true;
/******/ 			},
/******/ 			dispose: function(callback) {
/******/ 				hot._disposeHandlers.push(callback);
/******/ 			},
/******/ 			addDisposeHandler: function(callback) {
/******/ 				hot._disposeHandlers.push(callback);
/******/ 			},
/******/ 			removeDisposeHandler: function(callback) {
/******/ 				var idx = hot._disposeHandlers.indexOf(callback);
/******/ 				if (idx >= 0) hot._disposeHandlers.splice(idx, 1);
/******/ 			},
/******/
/******/ 			// Management API
/******/ 			check: hotCheck,
/******/ 			apply: hotApply,
/******/ 			status: function(l) {
/******/ 				if (!l) return hotStatus;
/******/ 				hotStatusHandlers.push(l);
/******/ 			},
/******/ 			addStatusHandler: function(l) {
/******/ 				hotStatusHandlers.push(l);
/******/ 			},
/******/ 			removeStatusHandler: function(l) {
/******/ 				var idx = hotStatusHandlers.indexOf(l);
/******/ 				if (idx >= 0) hotStatusHandlers.splice(idx, 1);
/******/ 			},
/******/
/******/ 			//inherit from previous dispose call
/******/ 			data: hotCurrentModuleData[moduleId]
/******/ 		};
/******/ 		hotCurrentChildModule = undefined;
/******/ 		return hot;
/******/ 	}
/******/
/******/ 	var hotStatusHandlers = [];
/******/ 	var hotStatus = "idle";
/******/
/******/ 	function hotSetStatus(newStatus) {
/******/ 		hotStatus = newStatus;
/******/ 		for (var i = 0; i < hotStatusHandlers.length; i++)
/******/ 			hotStatusHandlers[i].call(null, newStatus);
/******/ 	}
/******/
/******/ 	// while downloading
/******/ 	var hotWaitingFiles = 0;
/******/ 	var hotChunksLoading = 0;
/******/ 	var hotWaitingFilesMap = {};
/******/ 	var hotRequestedFilesMap = {};
/******/ 	var hotAvailableFilesMap = {};
/******/ 	var hotDeferred;
/******/
/******/ 	// The update info
/******/ 	var hotUpdate, hotUpdateNewHash;
/******/
/******/ 	function toModuleId(id) {
/******/ 		var isNumber = +id + "" === id;
/******/ 		return isNumber ? +id : id;
/******/ 	}
/******/
/******/ 	function hotCheck(apply) {
/******/ 		if (hotStatus !== "idle") {
/******/ 			throw new Error("check() is only allowed in idle status");
/******/ 		}
/******/ 		hotApplyOnUpdate = apply;
/******/ 		hotSetStatus("check");
/******/ 		return hotDownloadManifest(hotRequestTimeout).then(function(update) {
/******/ 			if (!update) {
/******/ 				hotSetStatus("idle");
/******/ 				return null;
/******/ 			}
/******/ 			hotRequestedFilesMap = {};
/******/ 			hotWaitingFilesMap = {};
/******/ 			hotAvailableFilesMap = update.c;
/******/ 			hotUpdateNewHash = update.h;
/******/
/******/ 			hotSetStatus("prepare");
/******/ 			var promise = new Promise(function(resolve, reject) {
/******/ 				hotDeferred = {
/******/ 					resolve: resolve,
/******/ 					reject: reject
/******/ 				};
/******/ 			});
/******/ 			hotUpdate = {};
/******/ 			for(var chunkId in installedChunks)
/******/ 			// eslint-disable-next-line no-lone-blocks
/******/ 			{
/******/ 				/*globals chunkId */
/******/ 				hotEnsureUpdateChunk(chunkId);
/******/ 			}
/******/ 			if (
/******/ 				hotStatus === "prepare" &&
/******/ 				hotChunksLoading === 0 &&
/******/ 				hotWaitingFiles === 0
/******/ 			) {
/******/ 				hotUpdateDownloaded();
/******/ 			}
/******/ 			return promise;
/******/ 		});
/******/ 	}
/******/
/******/ 	// eslint-disable-next-line no-unused-vars
/******/ 	function hotAddUpdateChunk(chunkId, moreModules) {
/******/ 		if (!hotAvailableFilesMap[chunkId] || !hotRequestedFilesMap[chunkId])
/******/ 			return;
/******/ 		hotRequestedFilesMap[chunkId] = false;
/******/ 		for (var moduleId in moreModules) {
/******/ 			if (Object.prototype.hasOwnProperty.call(moreModules, moduleId)) {
/******/ 				hotUpdate[moduleId] = moreModules[moduleId];
/******/ 			}
/******/ 		}
/******/ 		if (--hotWaitingFiles === 0 && hotChunksLoading === 0) {
/******/ 			hotUpdateDownloaded();
/******/ 		}
/******/ 	}
/******/
/******/ 	function hotEnsureUpdateChunk(chunkId) {
/******/ 		if (!hotAvailableFilesMap[chunkId]) {
/******/ 			hotWaitingFilesMap[chunkId] = true;
/******/ 		} else {
/******/ 			hotRequestedFilesMap[chunkId] = true;
/******/ 			hotWaitingFiles++;
/******/ 			hotDownloadUpdateChunk(chunkId);
/******/ 		}
/******/ 	}
/******/
/******/ 	function hotUpdateDownloaded() {
/******/ 		hotSetStatus("ready");
/******/ 		var deferred = hotDeferred;
/******/ 		hotDeferred = null;
/******/ 		if (!deferred) return;
/******/ 		if (hotApplyOnUpdate) {
/******/ 			// Wrap deferred object in Promise to mark it as a well-handled Promise to
/******/ 			// avoid triggering uncaught exception warning in Chrome.
/******/ 			// See https://bugs.chromium.org/p/chromium/issues/detail?id=465666
/******/ 			Promise.resolve()
/******/ 				.then(function() {
/******/ 					return hotApply(hotApplyOnUpdate);
/******/ 				})
/******/ 				.then(
/******/ 					function(result) {
/******/ 						deferred.resolve(result);
/******/ 					},
/******/ 					function(err) {
/******/ 						deferred.reject(err);
/******/ 					}
/******/ 				);
/******/ 		} else {
/******/ 			var outdatedModules = [];
/******/ 			for (var id in hotUpdate) {
/******/ 				if (Object.prototype.hasOwnProperty.call(hotUpdate, id)) {
/******/ 					outdatedModules.push(toModuleId(id));
/******/ 				}
/******/ 			}
/******/ 			deferred.resolve(outdatedModules);
/******/ 		}
/******/ 	}
/******/
/******/ 	function hotApply(options) {
/******/ 		if (hotStatus !== "ready")
/******/ 			throw new Error("apply() is only allowed in ready status");
/******/ 		options = options || {};
/******/
/******/ 		var cb;
/******/ 		var i;
/******/ 		var j;
/******/ 		var module;
/******/ 		var moduleId;
/******/
/******/ 		function getAffectedStuff(updateModuleId) {
/******/ 			var outdatedModules = [updateModuleId];
/******/ 			var outdatedDependencies = {};
/******/
/******/ 			var queue = outdatedModules.slice().map(function(id) {
/******/ 				return {
/******/ 					chain: [id],
/******/ 					id: id
/******/ 				};
/******/ 			});
/******/ 			while (queue.length > 0) {
/******/ 				var queueItem = queue.pop();
/******/ 				var moduleId = queueItem.id;
/******/ 				var chain = queueItem.chain;
/******/ 				module = installedModules[moduleId];
/******/ 				if (!module || module.hot._selfAccepted) continue;
/******/ 				if (module.hot._selfDeclined) {
/******/ 					return {
/******/ 						type: "self-declined",
/******/ 						chain: chain,
/******/ 						moduleId: moduleId
/******/ 					};
/******/ 				}
/******/ 				if (module.hot._main) {
/******/ 					return {
/******/ 						type: "unaccepted",
/******/ 						chain: chain,
/******/ 						moduleId: moduleId
/******/ 					};
/******/ 				}
/******/ 				for (var i = 0; i < module.parents.length; i++) {
/******/ 					var parentId = module.parents[i];
/******/ 					var parent = installedModules[parentId];
/******/ 					if (!parent) continue;
/******/ 					if (parent.hot._declinedDependencies[moduleId]) {
/******/ 						return {
/******/ 							type: "declined",
/******/ 							chain: chain.concat([parentId]),
/******/ 							moduleId: moduleId,
/******/ 							parentId: parentId
/******/ 						};
/******/ 					}
/******/ 					if (outdatedModules.indexOf(parentId) !== -1) continue;
/******/ 					if (parent.hot._acceptedDependencies[moduleId]) {
/******/ 						if (!outdatedDependencies[parentId])
/******/ 							outdatedDependencies[parentId] = [];
/******/ 						addAllToSet(outdatedDependencies[parentId], [moduleId]);
/******/ 						continue;
/******/ 					}
/******/ 					delete outdatedDependencies[parentId];
/******/ 					outdatedModules.push(parentId);
/******/ 					queue.push({
/******/ 						chain: chain.concat([parentId]),
/******/ 						id: parentId
/******/ 					});
/******/ 				}
/******/ 			}
/******/
/******/ 			return {
/******/ 				type: "accepted",
/******/ 				moduleId: updateModuleId,
/******/ 				outdatedModules: outdatedModules,
/******/ 				outdatedDependencies: outdatedDependencies
/******/ 			};
/******/ 		}
/******/
/******/ 		function addAllToSet(a, b) {
/******/ 			for (var i = 0; i < b.length; i++) {
/******/ 				var item = b[i];
/******/ 				if (a.indexOf(item) === -1) a.push(item);
/******/ 			}
/******/ 		}
/******/
/******/ 		// at begin all updates modules are outdated
/******/ 		// the "outdated" status can propagate to parents if they don't accept the children
/******/ 		var outdatedDependencies = {};
/******/ 		var outdatedModules = [];
/******/ 		var appliedUpdate = {};
/******/
/******/ 		var warnUnexpectedRequire = function warnUnexpectedRequire() {
/******/ 			console.warn(
/******/ 				"[HMR] unexpected require(" + result.moduleId + ") to disposed module"
/******/ 			);
/******/ 		};
/******/
/******/ 		for (var id in hotUpdate) {
/******/ 			if (Object.prototype.hasOwnProperty.call(hotUpdate, id)) {
/******/ 				moduleId = toModuleId(id);
/******/ 				/** @type {TODO} */
/******/ 				var result;
/******/ 				if (hotUpdate[id]) {
/******/ 					result = getAffectedStuff(moduleId);
/******/ 				} else {
/******/ 					result = {
/******/ 						type: "disposed",
/******/ 						moduleId: id
/******/ 					};
/******/ 				}
/******/ 				/** @type {Error|false} */
/******/ 				var abortError = false;
/******/ 				var doApply = false;
/******/ 				var doDispose = false;
/******/ 				var chainInfo = "";
/******/ 				if (result.chain) {
/******/ 					chainInfo = "\nUpdate propagation: " + result.chain.join(" -> ");
/******/ 				}
/******/ 				switch (result.type) {
/******/ 					case "self-declined":
/******/ 						if (options.onDeclined) options.onDeclined(result);
/******/ 						if (!options.ignoreDeclined)
/******/ 							abortError = new Error(
/******/ 								"Aborted because of self decline: " +
/******/ 									result.moduleId +
/******/ 									chainInfo
/******/ 							);
/******/ 						break;
/******/ 					case "declined":
/******/ 						if (options.onDeclined) options.onDeclined(result);
/******/ 						if (!options.ignoreDeclined)
/******/ 							abortError = new Error(
/******/ 								"Aborted because of declined dependency: " +
/******/ 									result.moduleId +
/******/ 									" in " +
/******/ 									result.parentId +
/******/ 									chainInfo
/******/ 							);
/******/ 						break;
/******/ 					case "unaccepted":
/******/ 						if (options.onUnaccepted) options.onUnaccepted(result);
/******/ 						if (!options.ignoreUnaccepted)
/******/ 							abortError = new Error(
/******/ 								"Aborted because " + moduleId + " is not accepted" + chainInfo
/******/ 							);
/******/ 						break;
/******/ 					case "accepted":
/******/ 						if (options.onAccepted) options.onAccepted(result);
/******/ 						doApply = true;
/******/ 						break;
/******/ 					case "disposed":
/******/ 						if (options.onDisposed) options.onDisposed(result);
/******/ 						doDispose = true;
/******/ 						break;
/******/ 					default:
/******/ 						throw new Error("Unexception type " + result.type);
/******/ 				}
/******/ 				if (abortError) {
/******/ 					hotSetStatus("abort");
/******/ 					return Promise.reject(abortError);
/******/ 				}
/******/ 				if (doApply) {
/******/ 					appliedUpdate[moduleId] = hotUpdate[moduleId];
/******/ 					addAllToSet(outdatedModules, result.outdatedModules);
/******/ 					for (moduleId in result.outdatedDependencies) {
/******/ 						if (
/******/ 							Object.prototype.hasOwnProperty.call(
/******/ 								result.outdatedDependencies,
/******/ 								moduleId
/******/ 							)
/******/ 						) {
/******/ 							if (!outdatedDependencies[moduleId])
/******/ 								outdatedDependencies[moduleId] = [];
/******/ 							addAllToSet(
/******/ 								outdatedDependencies[moduleId],
/******/ 								result.outdatedDependencies[moduleId]
/******/ 							);
/******/ 						}
/******/ 					}
/******/ 				}
/******/ 				if (doDispose) {
/******/ 					addAllToSet(outdatedModules, [result.moduleId]);
/******/ 					appliedUpdate[moduleId] = warnUnexpectedRequire;
/******/ 				}
/******/ 			}
/******/ 		}
/******/
/******/ 		// Store self accepted outdated modules to require them later by the module system
/******/ 		var outdatedSelfAcceptedModules = [];
/******/ 		for (i = 0; i < outdatedModules.length; i++) {
/******/ 			moduleId = outdatedModules[i];
/******/ 			if (
/******/ 				installedModules[moduleId] &&
/******/ 				installedModules[moduleId].hot._selfAccepted
/******/ 			)
/******/ 				outdatedSelfAcceptedModules.push({
/******/ 					module: moduleId,
/******/ 					errorHandler: installedModules[moduleId].hot._selfAccepted
/******/ 				});
/******/ 		}
/******/
/******/ 		// Now in "dispose" phase
/******/ 		hotSetStatus("dispose");
/******/ 		Object.keys(hotAvailableFilesMap).forEach(function(chunkId) {
/******/ 			if (hotAvailableFilesMap[chunkId] === false) {
/******/ 				hotDisposeChunk(chunkId);
/******/ 			}
/******/ 		});
/******/
/******/ 		var idx;
/******/ 		var queue = outdatedModules.slice();
/******/ 		while (queue.length > 0) {
/******/ 			moduleId = queue.pop();
/******/ 			module = installedModules[moduleId];
/******/ 			if (!module) continue;
/******/
/******/ 			var data = {};
/******/
/******/ 			// Call dispose handlers
/******/ 			var disposeHandlers = module.hot._disposeHandlers;
/******/ 			for (j = 0; j < disposeHandlers.length; j++) {
/******/ 				cb = disposeHandlers[j];
/******/ 				cb(data);
/******/ 			}
/******/ 			hotCurrentModuleData[moduleId] = data;
/******/
/******/ 			// disable module (this disables requires from this module)
/******/ 			module.hot.active = false;
/******/
/******/ 			// remove module from cache
/******/ 			delete installedModules[moduleId];
/******/
/******/ 			// when disposing there is no need to call dispose handler
/******/ 			delete outdatedDependencies[moduleId];
/******/
/******/ 			// remove "parents" references from all children
/******/ 			for (j = 0; j < module.children.length; j++) {
/******/ 				var child = installedModules[module.children[j]];
/******/ 				if (!child) continue;
/******/ 				idx = child.parents.indexOf(moduleId);
/******/ 				if (idx >= 0) {
/******/ 					child.parents.splice(idx, 1);
/******/ 				}
/******/ 			}
/******/ 		}
/******/
/******/ 		// remove outdated dependency from module children
/******/ 		var dependency;
/******/ 		var moduleOutdatedDependencies;
/******/ 		for (moduleId in outdatedDependencies) {
/******/ 			if (
/******/ 				Object.prototype.hasOwnProperty.call(outdatedDependencies, moduleId)
/******/ 			) {
/******/ 				module = installedModules[moduleId];
/******/ 				if (module) {
/******/ 					moduleOutdatedDependencies = outdatedDependencies[moduleId];
/******/ 					for (j = 0; j < moduleOutdatedDependencies.length; j++) {
/******/ 						dependency = moduleOutdatedDependencies[j];
/******/ 						idx = module.children.indexOf(dependency);
/******/ 						if (idx >= 0) module.children.splice(idx, 1);
/******/ 					}
/******/ 				}
/******/ 			}
/******/ 		}
/******/
/******/ 		// Not in "apply" phase
/******/ 		hotSetStatus("apply");
/******/
/******/ 		hotCurrentHash = hotUpdateNewHash;
/******/
/******/ 		// insert new code
/******/ 		for (moduleId in appliedUpdate) {
/******/ 			if (Object.prototype.hasOwnProperty.call(appliedUpdate, moduleId)) {
/******/ 				modules[moduleId] = appliedUpdate[moduleId];
/******/ 			}
/******/ 		}
/******/
/******/ 		// call accept handlers
/******/ 		var error = null;
/******/ 		for (moduleId in outdatedDependencies) {
/******/ 			if (
/******/ 				Object.prototype.hasOwnProperty.call(outdatedDependencies, moduleId)
/******/ 			) {
/******/ 				module = installedModules[moduleId];
/******/ 				if (module) {
/******/ 					moduleOutdatedDependencies = outdatedDependencies[moduleId];
/******/ 					var callbacks = [];
/******/ 					for (i = 0; i < moduleOutdatedDependencies.length; i++) {
/******/ 						dependency = moduleOutdatedDependencies[i];
/******/ 						cb = module.hot._acceptedDependencies[dependency];
/******/ 						if (cb) {
/******/ 							if (callbacks.indexOf(cb) !== -1) continue;
/******/ 							callbacks.push(cb);
/******/ 						}
/******/ 					}
/******/ 					for (i = 0; i < callbacks.length; i++) {
/******/ 						cb = callbacks[i];
/******/ 						try {
/******/ 							cb(moduleOutdatedDependencies);
/******/ 						} catch (err) {
/******/ 							if (options.onErrored) {
/******/ 								options.onErrored({
/******/ 									type: "accept-errored",
/******/ 									moduleId: moduleId,
/******/ 									dependencyId: moduleOutdatedDependencies[i],
/******/ 									error: err
/******/ 								});
/******/ 							}
/******/ 							if (!options.ignoreErrored) {
/******/ 								if (!error) error = err;
/******/ 							}
/******/ 						}
/******/ 					}
/******/ 				}
/******/ 			}
/******/ 		}
/******/
/******/ 		// Load self accepted modules
/******/ 		for (i = 0; i < outdatedSelfAcceptedModules.length; i++) {
/******/ 			var item = outdatedSelfAcceptedModules[i];
/******/ 			moduleId = item.module;
/******/ 			hotCurrentParents = [moduleId];
/******/ 			try {
/******/ 				__webpack_require__(moduleId);
/******/ 			} catch (err) {
/******/ 				if (typeof item.errorHandler === "function") {
/******/ 					try {
/******/ 						item.errorHandler(err);
/******/ 					} catch (err2) {
/******/ 						if (options.onErrored) {
/******/ 							options.onErrored({
/******/ 								type: "self-accept-error-handler-errored",
/******/ 								moduleId: moduleId,
/******/ 								error: err2,
/******/ 								originalError: err
/******/ 							});
/******/ 						}
/******/ 						if (!options.ignoreErrored) {
/******/ 							if (!error) error = err2;
/******/ 						}
/******/ 						if (!error) error = err;
/******/ 					}
/******/ 				} else {
/******/ 					if (options.onErrored) {
/******/ 						options.onErrored({
/******/ 							type: "self-accept-errored",
/******/ 							moduleId: moduleId,
/******/ 							error: err
/******/ 						});
/******/ 					}
/******/ 					if (!options.ignoreErrored) {
/******/ 						if (!error) error = err;
/******/ 					}
/******/ 				}
/******/ 			}
/******/ 		}
/******/
/******/ 		// handle errors in accept handlers and self accepted module load
/******/ 		if (error) {
/******/ 			hotSetStatus("fail");
/******/ 			return Promise.reject(error);
/******/ 		}
/******/
/******/ 		hotSetStatus("idle");
/******/ 		return new Promise(function(resolve) {
/******/ 			resolve(outdatedModules);
/******/ 		});
/******/ 	}
/******/
/******/ 	// The module cache
/******/ 	var installedModules = {};
/******/
/******/ 	// object to store loaded and loading chunks
/******/ 	// undefined = chunk not loaded, null = chunk preloaded/prefetched
/******/ 	// Promise = chunk loading, 0 = chunk loaded
/******/ 	var installedChunks = {
/******/ 		"preamble": 0
/******/ 	};
/******/
/******/ 	var deferredModules = [];
/******/
/******/ 	// The require function
/******/ 	function __webpack_require__(moduleId) {
/******/
/******/ 		// Check if module is in cache
/******/ 		if(installedModules[moduleId]) {
/******/ 			return installedModules[moduleId].exports;
/******/ 		}
/******/ 		// Create a new module (and put it into the cache)
/******/ 		var module = installedModules[moduleId] = {
/******/ 			i: moduleId,
/******/ 			l: false,
/******/ 			exports: {},
/******/ 			hot: hotCreateModule(moduleId),
/******/ 			parents: (hotCurrentParentsTemp = hotCurrentParents, hotCurrentParents = [], hotCurrentParentsTemp),
/******/ 			children: []
/******/ 		};
/******/
/******/ 		// Execute the module function
/******/ 		modules[moduleId].call(module.exports, module, module.exports, hotCreateRequire(moduleId));
/******/
/******/ 		// Flag the module as loaded
/******/ 		module.l = true;
/******/
/******/ 		// Return the exports of the module
/******/ 		return module.exports;
/******/ 	}
/******/
/******/
/******/ 	// expose the modules object (__webpack_modules__)
/******/ 	__webpack_require__.m = modules;
/******/
/******/ 	// expose the module cache
/******/ 	__webpack_require__.c = installedModules;
/******/
/******/ 	// define getter function for harmony exports
/******/ 	__webpack_require__.d = function(exports, name, getter) {
/******/ 		if(!__webpack_require__.o(exports, name)) {
/******/ 			Object.defineProperty(exports, name, { enumerable: true, get: getter });
/******/ 		}
/******/ 	};
/******/
/******/ 	// define __esModule on exports
/******/ 	__webpack_require__.r = function(exports) {
/******/ 		if(typeof Symbol !== 'undefined' && Symbol.toStringTag) {
/******/ 			Object.defineProperty(exports, Symbol.toStringTag, { value: 'Module' });
/******/ 		}
/******/ 		Object.defineProperty(exports, '__esModule', { value: true });
/******/ 	};
/******/
/******/ 	// create a fake namespace object
/******/ 	// mode & 1: value is a module id, require it
/******/ 	// mode & 2: merge all properties of value into the ns
/******/ 	// mode & 4: return value when already ns object
/******/ 	// mode & 8|1: behave like require
/******/ 	__webpack_require__.t = function(value, mode) {
/******/ 		if(mode & 1) value = __webpack_require__(value);
/******/ 		if(mode & 8) return value;
/******/ 		if((mode & 4) && typeof value === 'object' && value && value.__esModule) return value;
/******/ 		var ns = Object.create(null);
/******/ 		__webpack_require__.r(ns);
/******/ 		Object.defineProperty(ns, 'default', { enumerable: true, value: value });
/******/ 		if(mode & 2 && typeof value != 'string') for(var key in value) __webpack_require__.d(ns, key, function(key) { return value[key]; }.bind(null, key));
/******/ 		return ns;
/******/ 	};
/******/
/******/ 	// getDefaultExport function for compatibility with non-harmony modules
/******/ 	__webpack_require__.n = function(module) {
/******/ 		var getter = module && module.__esModule ?
/******/ 			function getDefault() { return module['default']; } :
/******/ 			function getModuleExports() { return module; };
/******/ 		__webpack_require__.d(getter, 'a', getter);
/******/ 		return getter;
/******/ 	};
/******/
/******/ 	// Object.prototype.hasOwnProperty.call
/******/ 	__webpack_require__.o = function(object, property) { return Object.prototype.hasOwnProperty.call(object, property); };
/******/
/******/ 	// __webpack_public_path__
/******/ 	__webpack_require__.p = "/static/assets/dist/";
/******/
/******/ 	// __webpack_hash__
/******/ 	__webpack_require__.h = function() { return hotCurrentHash; };
/******/
/******/ 	var jsonpArray = window["webpackJsonp"] = window["webpackJsonp"] || [];
/******/ 	var oldJsonpFunction = jsonpArray.push.bind(jsonpArray);
/******/ 	jsonpArray.push = webpackJsonpCallback;
/******/ 	jsonpArray = jsonpArray.slice();
/******/ 	for(var i = 0; i < jsonpArray.length; i++) webpackJsonpCallback(jsonpArray[i]);
/******/ 	var parentJsonpFunction = oldJsonpFunction;
/******/
/******/
/******/ 	// add entry module to deferred list
/******/ 	deferredModules.push([0,"vendors-major","vendors-addSlice-dashboard-explore-preamble-profile-sqllab-welcome"]);
/******/ 	// run deferred modules when ready
/******/ 	return checkDeferredModules();
/******/ })
/************************************************************************/
/******/ ({

/***/ "./src/preamble.js":
/*!*************************!*\
  !*** ./src/preamble.js ***!
  \*************************/
/*! no exports provided */
/***/ (function(module, __webpack_exports__, __webpack_require__) {

"use strict";
eval("__webpack_require__.r(__webpack_exports__);\n/* harmony import */ var abortcontroller_polyfill_dist_abortcontroller_polyfill_only__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! abortcontroller-polyfill/dist/abortcontroller-polyfill-only */ \"./node_modules/abortcontroller-polyfill/dist/abortcontroller-polyfill-only.js\");\n/* harmony import */ var abortcontroller_polyfill_dist_abortcontroller_polyfill_only__WEBPACK_IMPORTED_MODULE_0___default = /*#__PURE__*/__webpack_require__.n(abortcontroller_polyfill_dist_abortcontroller_polyfill_only__WEBPACK_IMPORTED_MODULE_0__);\n/* harmony import */ var _superset_ui_translation__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(/*! @superset-ui/translation */ \"./node_modules/@superset-ui/translation/esm/index.js\");\n/* harmony import */ var _setup_setupClient__WEBPACK_IMPORTED_MODULE_2__ = __webpack_require__(/*! ./setup/setupClient */ \"./src/setup/setupClient.js\");\n/* harmony import */ var _setup_setupColors__WEBPACK_IMPORTED_MODULE_3__ = __webpack_require__(/*! ./setup/setupColors */ \"./src/setup/setupColors.js\");\n/* harmony import */ var _setup_setupFormatters__WEBPACK_IMPORTED_MODULE_4__ = __webpack_require__(/*! ./setup/setupFormatters */ \"./src/setup/setupFormatters.js\");\n/**\n * Licensed to the Apache Software Foundation (ASF) under one\n * or more contributor license agreements.  See the NOTICE file\n * distributed with this work for additional information\n * regarding copyright ownership.  The ASF licenses this file\n * to you under the Apache License, Version 2.0 (the\n * \"License\"); you may not use this file except in compliance\n * with the License.  You may obtain a copy of the License at\n *\n *   http://www.apache.org/licenses/LICENSE-2.0\n *\n * Unless required by applicable law or agreed to in writing,\n * software distributed under the License is distributed on an\n * \"AS IS\" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY\n * KIND, either express or implied.  See the License for the\n * specific language governing permissions and limitations\n * under the License.\n */\n\n\n\n\n // Configure translation\n\nif (typeof window !== 'undefined') {\n  var root = document.getElementById('app');\n  var bootstrapData = root ? JSON.parse(root.getAttribute('data-bootstrap')) : {};\n\n  if (bootstrapData.common && bootstrapData.common.language_pack) {\n    var languagePack = bootstrapData.common.language_pack;\n    Object(_superset_ui_translation__WEBPACK_IMPORTED_MODULE_1__[\"configure\"])({\n      languagePack: languagePack\n    });\n  } else {\n    Object(_superset_ui_translation__WEBPACK_IMPORTED_MODULE_1__[\"configure\"])();\n  }\n} else {\n  Object(_superset_ui_translation__WEBPACK_IMPORTED_MODULE_1__[\"configure\"])();\n} // Setup SupersetClient\n\n\nObject(_setup_setupClient__WEBPACK_IMPORTED_MODULE_2__[\"default\"])(); // Setup color palettes\n\nObject(_setup_setupColors__WEBPACK_IMPORTED_MODULE_3__[\"default\"])(); // Setup number formatters\n\nObject(_setup_setupFormatters__WEBPACK_IMPORTED_MODULE_4__[\"default\"])();//# sourceURL=[module]\n//# sourceMappingURL=data:application/json;charset=utf-8;base64,eyJ2ZXJzaW9uIjozLCJmaWxlIjoiLi9zcmMvcHJlYW1ibGUuanMuanMiLCJzb3VyY2VzIjpbIndlYnBhY2s6Ly8vLi9zcmMvcHJlYW1ibGUuanM/Mjc0NCJdLCJzb3VyY2VzQ29udGVudCI6WyIvKipcbiAqIExpY2Vuc2VkIHRvIHRoZSBBcGFjaGUgU29mdHdhcmUgRm91bmRhdGlvbiAoQVNGKSB1bmRlciBvbmVcbiAqIG9yIG1vcmUgY29udHJpYnV0b3IgbGljZW5zZSBhZ3JlZW1lbnRzLiAgU2VlIHRoZSBOT1RJQ0UgZmlsZVxuICogZGlzdHJpYnV0ZWQgd2l0aCB0aGlzIHdvcmsgZm9yIGFkZGl0aW9uYWwgaW5mb3JtYXRpb25cbiAqIHJlZ2FyZGluZyBjb3B5cmlnaHQgb3duZXJzaGlwLiAgVGhlIEFTRiBsaWNlbnNlcyB0aGlzIGZpbGVcbiAqIHRvIHlvdSB1bmRlciB0aGUgQXBhY2hlIExpY2Vuc2UsIFZlcnNpb24gMi4wICh0aGVcbiAqIFwiTGljZW5zZVwiKTsgeW91IG1heSBub3QgdXNlIHRoaXMgZmlsZSBleGNlcHQgaW4gY29tcGxpYW5jZVxuICogd2l0aCB0aGUgTGljZW5zZS4gIFlvdSBtYXkgb2J0YWluIGEgY29weSBvZiB0aGUgTGljZW5zZSBhdFxuICpcbiAqICAgaHR0cDovL3d3dy5hcGFjaGUub3JnL2xpY2Vuc2VzL0xJQ0VOU0UtMi4wXG4gKlxuICogVW5sZXNzIHJlcXVpcmVkIGJ5IGFwcGxpY2FibGUgbGF3IG9yIGFncmVlZCB0byBpbiB3cml0aW5nLFxuICogc29mdHdhcmUgZGlzdHJpYnV0ZWQgdW5kZXIgdGhlIExpY2Vuc2UgaXMgZGlzdHJpYnV0ZWQgb24gYW5cbiAqIFwiQVMgSVNcIiBCQVNJUywgV0lUSE9VVCBXQVJSQU5USUVTIE9SIENPTkRJVElPTlMgT0YgQU5ZXG4gKiBLSU5ELCBlaXRoZXIgZXhwcmVzcyBvciBpbXBsaWVkLiAgU2VlIHRoZSBMaWNlbnNlIGZvciB0aGVcbiAqIHNwZWNpZmljIGxhbmd1YWdlIGdvdmVybmluZyBwZXJtaXNzaW9ucyBhbmQgbGltaXRhdGlvbnNcbiAqIHVuZGVyIHRoZSBMaWNlbnNlLlxuICovXG5pbXBvcnQgJ2Fib3J0Y29udHJvbGxlci1wb2x5ZmlsbC9kaXN0L2Fib3J0Y29udHJvbGxlci1wb2x5ZmlsbC1vbmx5JztcbmltcG9ydCB7IGNvbmZpZ3VyZSB9IGZyb20gJ0BzdXBlcnNldC11aS90cmFuc2xhdGlvbic7XG5pbXBvcnQgc2V0dXBDbGllbnQgZnJvbSAnLi9zZXR1cC9zZXR1cENsaWVudCc7XG5pbXBvcnQgc2V0dXBDb2xvcnMgZnJvbSAnLi9zZXR1cC9zZXR1cENvbG9ycyc7XG5pbXBvcnQgc2V0dXBGb3JtYXR0ZXJzIGZyb20gJy4vc2V0dXAvc2V0dXBGb3JtYXR0ZXJzJztcblxuLy8gQ29uZmlndXJlIHRyYW5zbGF0aW9uXG5pZiAodHlwZW9mIHdpbmRvdyAhPT0gJ3VuZGVmaW5lZCcpIHtcbiAgY29uc3Qgcm9vdCA9IGRvY3VtZW50LmdldEVsZW1lbnRCeUlkKCdhcHAnKTtcbiAgY29uc3QgYm9vdHN0cmFwRGF0YSA9IHJvb3QgPyBKU09OLnBhcnNlKHJvb3QuZ2V0QXR0cmlidXRlKCdkYXRhLWJvb3RzdHJhcCcpKSA6IHt9O1xuICBpZiAoYm9vdHN0cmFwRGF0YS5jb21tb24gJiYgYm9vdHN0cmFwRGF0YS5jb21tb24ubGFuZ3VhZ2VfcGFjaykge1xuICAgIGNvbnN0IGxhbmd1YWdlUGFjayA9IGJvb3RzdHJhcERhdGEuY29tbW9uLmxhbmd1YWdlX3BhY2s7XG4gICAgY29uZmlndXJlKHsgbGFuZ3VhZ2VQYWNrIH0pO1xuICB9IGVsc2Uge1xuICAgIGNvbmZpZ3VyZSgpO1xuICB9XG59IGVsc2Uge1xuICBjb25maWd1cmUoKTtcbn1cblxuLy8gU2V0dXAgU3VwZXJzZXRDbGllbnRcbnNldHVwQ2xpZW50KCk7XG5cbi8vIFNldHVwIGNvbG9yIHBhbGV0dGVzXG5zZXR1cENvbG9ycygpO1xuXG4vLyBTZXR1cCBudW1iZXIgZm9ybWF0dGVyc1xuc2V0dXBGb3JtYXR0ZXJzKCk7XG4iXSwibWFwcGluZ3MiOiJBQUFBO0FBQUE7QUFBQTtBQUFBO0FBQUE7QUFBQTtBQUFBO0FBQUE7Ozs7Ozs7Ozs7Ozs7Ozs7OztBQWtCQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFFQTtBQUNBO0FBQ0E7QUFDQTtBQUFBO0FBQ0E7QUFDQTtBQUFBO0FBQUE7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUVBO0FBQ0E7QUFFQSIsInNvdXJjZVJvb3QiOiIifQ==\n//# sourceURL=webpack-internal:///./src/preamble.js\n");

/***/ }),

/***/ "./src/setup/setupClient.js":
/*!**********************************!*\
  !*** ./src/setup/setupClient.js ***!
  \**********************************/
/*! exports provided: default */
/***/ (function(module, __webpack_exports__, __webpack_require__) {

"use strict";
eval("__webpack_require__.r(__webpack_exports__);\n/* WEBPACK VAR INJECTION */(function(module) {/* harmony export (binding) */ __webpack_require__.d(__webpack_exports__, \"default\", function() { return setupClient; });\n/* harmony import */ var _superset_ui_connection__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! @superset-ui/connection */ \"./node_modules/@superset-ui/connection/esm/index.js\");\n(function () {\n  var enterModule = __webpack_require__(/*! react-hot-loader */ \"./node_modules/react-hot-loader/index.js\").enterModule;\n\n  enterModule && enterModule(module);\n})();\n\n/**\n * Licensed to the Apache Software Foundation (ASF) under one\n * or more contributor license agreements.  See the NOTICE file\n * distributed with this work for additional information\n * regarding copyright ownership.  The ASF licenses this file\n * to you under the Apache License, Version 2.0 (the\n * \"License\"); you may not use this file except in compliance\n * with the License.  You may obtain a copy of the License at\n *\n *   http://www.apache.org/licenses/LICENSE-2.0\n *\n * Unless required by applicable law or agreed to in writing,\n * software distributed under the License is distributed on an\n * \"AS IS\" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY\n * KIND, either express or implied.  See the License for the\n * specific language governing permissions and limitations\n * under the License.\n */\n\n/* eslint no-console: 0 */\n\nfunction setupClient() {\n  var csrfNode = document.querySelector('#csrf_token');\n  var csrfToken = csrfNode ? csrfNode.value : null;\n  _superset_ui_connection__WEBPACK_IMPORTED_MODULE_0__[\"SupersetClient\"].configure({\n    protocol: window.location && window.location.protocol || '',\n    host: window.location && window.location.host || '',\n    csrfToken: csrfToken\n  }).init()[\"catch\"](function (error) {\n    console.warn('Error initializing SupersetClient', error);\n  });\n}\n;\n\n(function () {\n  var reactHotLoader = __webpack_require__(/*! react-hot-loader */ \"./node_modules/react-hot-loader/index.js\").default;\n\n  var leaveModule = __webpack_require__(/*! react-hot-loader */ \"./node_modules/react-hot-loader/index.js\").leaveModule;\n\n  if (!reactHotLoader) {\n    return;\n  }\n\n  reactHotLoader.register(setupClient, \"setupClient\", \"/home/leonardo/proyectos/dashboard/incubator-superset/superset/assets/src/setup/setupClient.js\");\n  leaveModule(module);\n})();\n\n;\n/* WEBPACK VAR INJECTION */}.call(this, __webpack_require__(/*! ./../../node_modules/webpack/buildin/harmony-module.js */ \"./node_modules/webpack/buildin/harmony-module.js\")(module)))//# sourceURL=[module]\n//# sourceMappingURL=data:application/json;charset=utf-8;base64,eyJ2ZXJzaW9uIjozLCJmaWxlIjoiLi9zcmMvc2V0dXAvc2V0dXBDbGllbnQuanMuanMiLCJzb3VyY2VzIjpbIndlYnBhY2s6Ly8vLi9zcmMvc2V0dXAvc2V0dXBDbGllbnQuanM/ZDY5ZSJdLCJzb3VyY2VzQ29udGVudCI6WyIvKipcbiAqIExpY2Vuc2VkIHRvIHRoZSBBcGFjaGUgU29mdHdhcmUgRm91bmRhdGlvbiAoQVNGKSB1bmRlciBvbmVcbiAqIG9yIG1vcmUgY29udHJpYnV0b3IgbGljZW5zZSBhZ3JlZW1lbnRzLiAgU2VlIHRoZSBOT1RJQ0UgZmlsZVxuICogZGlzdHJpYnV0ZWQgd2l0aCB0aGlzIHdvcmsgZm9yIGFkZGl0aW9uYWwgaW5mb3JtYXRpb25cbiAqIHJlZ2FyZGluZyBjb3B5cmlnaHQgb3duZXJzaGlwLiAgVGhlIEFTRiBsaWNlbnNlcyB0aGlzIGZpbGVcbiAqIHRvIHlvdSB1bmRlciB0aGUgQXBhY2hlIExpY2Vuc2UsIFZlcnNpb24gMi4wICh0aGVcbiAqIFwiTGljZW5zZVwiKTsgeW91IG1heSBub3QgdXNlIHRoaXMgZmlsZSBleGNlcHQgaW4gY29tcGxpYW5jZVxuICogd2l0aCB0aGUgTGljZW5zZS4gIFlvdSBtYXkgb2J0YWluIGEgY29weSBvZiB0aGUgTGljZW5zZSBhdFxuICpcbiAqICAgaHR0cDovL3d3dy5hcGFjaGUub3JnL2xpY2Vuc2VzL0xJQ0VOU0UtMi4wXG4gKlxuICogVW5sZXNzIHJlcXVpcmVkIGJ5IGFwcGxpY2FibGUgbGF3IG9yIGFncmVlZCB0byBpbiB3cml0aW5nLFxuICogc29mdHdhcmUgZGlzdHJpYnV0ZWQgdW5kZXIgdGhlIExpY2Vuc2UgaXMgZGlzdHJpYnV0ZWQgb24gYW5cbiAqIFwiQVMgSVNcIiBCQVNJUywgV0lUSE9VVCBXQVJSQU5USUVTIE9SIENPTkRJVElPTlMgT0YgQU5ZXG4gKiBLSU5ELCBlaXRoZXIgZXhwcmVzcyBvciBpbXBsaWVkLiAgU2VlIHRoZSBMaWNlbnNlIGZvciB0aGVcbiAqIHNwZWNpZmljIGxhbmd1YWdlIGdvdmVybmluZyBwZXJtaXNzaW9ucyBhbmQgbGltaXRhdGlvbnNcbiAqIHVuZGVyIHRoZSBMaWNlbnNlLlxuICovXG4vKiBlc2xpbnQgbm8tY29uc29sZTogMCAqL1xuaW1wb3J0IHsgU3VwZXJzZXRDbGllbnQgfSBmcm9tICdAc3VwZXJzZXQtdWkvY29ubmVjdGlvbic7XG5cbmV4cG9ydCBkZWZhdWx0IGZ1bmN0aW9uIHNldHVwQ2xpZW50KCkge1xuICBjb25zdCBjc3JmTm9kZSA9IGRvY3VtZW50LnF1ZXJ5U2VsZWN0b3IoJyNjc3JmX3Rva2VuJyk7XG4gIGNvbnN0IGNzcmZUb2tlbiA9IGNzcmZOb2RlID8gY3NyZk5vZGUudmFsdWUgOiBudWxsO1xuXG4gIFN1cGVyc2V0Q2xpZW50LmNvbmZpZ3VyZSh7XG4gICAgcHJvdG9jb2w6ICh3aW5kb3cubG9jYXRpb24gJiYgd2luZG93LmxvY2F0aW9uLnByb3RvY29sKSB8fCAnJyxcbiAgICBob3N0OiAod2luZG93LmxvY2F0aW9uICYmIHdpbmRvdy5sb2NhdGlvbi5ob3N0KSB8fCAnJyxcbiAgICBjc3JmVG9rZW4sXG4gIH0pXG4gICAgLmluaXQoKVxuICAgIC5jYXRjaCgoZXJyb3IpID0+IHtcbiAgICAgIGNvbnNvbGUud2FybignRXJyb3IgaW5pdGlhbGl6aW5nIFN1cGVyc2V0Q2xpZW50JywgZXJyb3IpO1xuICAgIH0pO1xufVxuIl0sIm1hcHBpbmdzIjoiOzs7Ozs7Ozs7QUFBQTs7Ozs7Ozs7Ozs7Ozs7Ozs7OztBQWtCQTtBQUNBO0FBRUE7QUFDQTtBQUNBO0FBRUE7QUFDQTtBQUNBO0FBQ0E7QUFIQTtBQU9BO0FBQ0E7QUFDQTs7Ozs7Ozs7Ozs7O0FBYkE7Ozs7O0EiLCJzb3VyY2VSb290IjoiIn0=\n//# sourceURL=webpack-internal:///./src/setup/setupClient.js\n");

/***/ }),

/***/ "./src/setup/setupColors.js":
/*!**********************************!*\
  !*** ./src/setup/setupColors.js ***!
  \**********************************/
/*! exports provided: default */
/***/ (function(module, __webpack_exports__, __webpack_require__) {

"use strict";
eval("__webpack_require__.r(__webpack_exports__);\n/* WEBPACK VAR INJECTION */(function(module) {/* harmony export (binding) */ __webpack_require__.d(__webpack_exports__, \"default\", function() { return setupColors; });\n/* harmony import */ var _superset_ui_color_esm_colorSchemes_categorical_airbnb__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! @superset-ui/color/esm/colorSchemes/categorical/airbnb */ \"./node_modules/@superset-ui/color/esm/colorSchemes/categorical/airbnb.js\");\n/* harmony import */ var _superset_ui_color_esm_colorSchemes_categorical_d3__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(/*! @superset-ui/color/esm/colorSchemes/categorical/d3 */ \"./node_modules/@superset-ui/color/esm/colorSchemes/categorical/d3.js\");\n/* harmony import */ var _superset_ui_color_esm_colorSchemes_categorical_google__WEBPACK_IMPORTED_MODULE_2__ = __webpack_require__(/*! @superset-ui/color/esm/colorSchemes/categorical/google */ \"./node_modules/@superset-ui/color/esm/colorSchemes/categorical/google.js\");\n/* harmony import */ var _superset_ui_color_esm_colorSchemes_categorical_lyft__WEBPACK_IMPORTED_MODULE_3__ = __webpack_require__(/*! @superset-ui/color/esm/colorSchemes/categorical/lyft */ \"./node_modules/@superset-ui/color/esm/colorSchemes/categorical/lyft.js\");\n/* harmony import */ var _superset_ui_color_esm_colorSchemes_sequential_common__WEBPACK_IMPORTED_MODULE_4__ = __webpack_require__(/*! @superset-ui/color/esm/colorSchemes/sequential/common */ \"./node_modules/@superset-ui/color/esm/colorSchemes/sequential/common.js\");\n/* harmony import */ var _superset_ui_color_esm_colorSchemes_sequential_d3__WEBPACK_IMPORTED_MODULE_5__ = __webpack_require__(/*! @superset-ui/color/esm/colorSchemes/sequential/d3 */ \"./node_modules/@superset-ui/color/esm/colorSchemes/sequential/d3.js\");\n/* harmony import */ var _superset_ui_color__WEBPACK_IMPORTED_MODULE_6__ = __webpack_require__(/*! @superset-ui/color */ \"./node_modules/@superset-ui/color/esm/index.js\");\n(function () {\n  var enterModule = __webpack_require__(/*! react-hot-loader */ \"./node_modules/react-hot-loader/index.js\").enterModule;\n\n  enterModule && enterModule(module);\n})();\n\n/**\n * Licensed to the Apache Software Foundation (ASF) under one\n * or more contributor license agreements.  See the NOTICE file\n * distributed with this work for additional information\n * regarding copyright ownership.  The ASF licenses this file\n * to you under the Apache License, Version 2.0 (the\n * \"License\"); you may not use this file except in compliance\n * with the License.  You may obtain a copy of the License at\n *\n *   http://www.apache.org/licenses/LICENSE-2.0\n *\n * Unless required by applicable law or agreed to in writing,\n * software distributed under the License is distributed on an\n * \"AS IS\" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY\n * KIND, either express or implied.  See the License for the\n * specific language governing permissions and limitations\n * under the License.\n */\n\n\n\n\n\n\n\nfunction setupColors() {\n  // Register color schemes\n  var categoricalSchemeRegistry = Object(_superset_ui_color__WEBPACK_IMPORTED_MODULE_6__[\"getCategoricalSchemeRegistry\"])();\n  [_superset_ui_color_esm_colorSchemes_categorical_airbnb__WEBPACK_IMPORTED_MODULE_0__[\"default\"], _superset_ui_color_esm_colorSchemes_categorical_d3__WEBPACK_IMPORTED_MODULE_1__[\"default\"], _superset_ui_color_esm_colorSchemes_categorical_google__WEBPACK_IMPORTED_MODULE_2__[\"default\"], _superset_ui_color_esm_colorSchemes_categorical_lyft__WEBPACK_IMPORTED_MODULE_3__[\"default\"]].forEach(function (group) {\n    group.forEach(function (scheme) {\n      categoricalSchemeRegistry.registerValue(scheme.id, scheme);\n    });\n  });\n  categoricalSchemeRegistry.setDefaultKey('bnbColors');\n  var sequentialSchemeRegistry = Object(_superset_ui_color__WEBPACK_IMPORTED_MODULE_6__[\"getSequentialSchemeRegistry\"])();\n  [_superset_ui_color_esm_colorSchemes_sequential_common__WEBPACK_IMPORTED_MODULE_4__[\"default\"], _superset_ui_color_esm_colorSchemes_sequential_d3__WEBPACK_IMPORTED_MODULE_5__[\"default\"]].forEach(function (group) {\n    group.forEach(function (scheme) {\n      sequentialSchemeRegistry.registerValue(scheme.id, scheme);\n    });\n  });\n}\n;\n\n(function () {\n  var reactHotLoader = __webpack_require__(/*! react-hot-loader */ \"./node_modules/react-hot-loader/index.js\").default;\n\n  var leaveModule = __webpack_require__(/*! react-hot-loader */ \"./node_modules/react-hot-loader/index.js\").leaveModule;\n\n  if (!reactHotLoader) {\n    return;\n  }\n\n  reactHotLoader.register(setupColors, \"setupColors\", \"/home/leonardo/proyectos/dashboard/incubator-superset/superset/assets/src/setup/setupColors.js\");\n  leaveModule(module);\n})();\n\n;\n/* WEBPACK VAR INJECTION */}.call(this, __webpack_require__(/*! ./../../node_modules/webpack/buildin/harmony-module.js */ \"./node_modules/webpack/buildin/harmony-module.js\")(module)))//# sourceURL=[module]\n//# sourceMappingURL=data:application/json;charset=utf-8;base64,eyJ2ZXJzaW9uIjozLCJmaWxlIjoiLi9zcmMvc2V0dXAvc2V0dXBDb2xvcnMuanMuanMiLCJzb3VyY2VzIjpbIndlYnBhY2s6Ly8vLi9zcmMvc2V0dXAvc2V0dXBDb2xvcnMuanM/NjQzNiJdLCJzb3VyY2VzQ29udGVudCI6WyIvKipcbiAqIExpY2Vuc2VkIHRvIHRoZSBBcGFjaGUgU29mdHdhcmUgRm91bmRhdGlvbiAoQVNGKSB1bmRlciBvbmVcbiAqIG9yIG1vcmUgY29udHJpYnV0b3IgbGljZW5zZSBhZ3JlZW1lbnRzLiAgU2VlIHRoZSBOT1RJQ0UgZmlsZVxuICogZGlzdHJpYnV0ZWQgd2l0aCB0aGlzIHdvcmsgZm9yIGFkZGl0aW9uYWwgaW5mb3JtYXRpb25cbiAqIHJlZ2FyZGluZyBjb3B5cmlnaHQgb3duZXJzaGlwLiAgVGhlIEFTRiBsaWNlbnNlcyB0aGlzIGZpbGVcbiAqIHRvIHlvdSB1bmRlciB0aGUgQXBhY2hlIExpY2Vuc2UsIFZlcnNpb24gMi4wICh0aGVcbiAqIFwiTGljZW5zZVwiKTsgeW91IG1heSBub3QgdXNlIHRoaXMgZmlsZSBleGNlcHQgaW4gY29tcGxpYW5jZVxuICogd2l0aCB0aGUgTGljZW5zZS4gIFlvdSBtYXkgb2J0YWluIGEgY29weSBvZiB0aGUgTGljZW5zZSBhdFxuICpcbiAqICAgaHR0cDovL3d3dy5hcGFjaGUub3JnL2xpY2Vuc2VzL0xJQ0VOU0UtMi4wXG4gKlxuICogVW5sZXNzIHJlcXVpcmVkIGJ5IGFwcGxpY2FibGUgbGF3IG9yIGFncmVlZCB0byBpbiB3cml0aW5nLFxuICogc29mdHdhcmUgZGlzdHJpYnV0ZWQgdW5kZXIgdGhlIExpY2Vuc2UgaXMgZGlzdHJpYnV0ZWQgb24gYW5cbiAqIFwiQVMgSVNcIiBCQVNJUywgV0lUSE9VVCBXQVJSQU5USUVTIE9SIENPTkRJVElPTlMgT0YgQU5ZXG4gKiBLSU5ELCBlaXRoZXIgZXhwcmVzcyBvciBpbXBsaWVkLiAgU2VlIHRoZSBMaWNlbnNlIGZvciB0aGVcbiAqIHNwZWNpZmljIGxhbmd1YWdlIGdvdmVybmluZyBwZXJtaXNzaW9ucyBhbmQgbGltaXRhdGlvbnNcbiAqIHVuZGVyIHRoZSBMaWNlbnNlLlxuICovXG5pbXBvcnQgYWlyYm5iIGZyb20gJ0BzdXBlcnNldC11aS9jb2xvci9lc20vY29sb3JTY2hlbWVzL2NhdGVnb3JpY2FsL2FpcmJuYic7XG5pbXBvcnQgY2F0ZWdvcmljYWxEMyBmcm9tICdAc3VwZXJzZXQtdWkvY29sb3IvZXNtL2NvbG9yU2NoZW1lcy9jYXRlZ29yaWNhbC9kMyc7XG5pbXBvcnQgZ29vZ2xlIGZyb20gJ0BzdXBlcnNldC11aS9jb2xvci9lc20vY29sb3JTY2hlbWVzL2NhdGVnb3JpY2FsL2dvb2dsZSc7XG5pbXBvcnQgbHlmdCBmcm9tICdAc3VwZXJzZXQtdWkvY29sb3IvZXNtL2NvbG9yU2NoZW1lcy9jYXRlZ29yaWNhbC9seWZ0JztcbmltcG9ydCBzZXF1ZW50aWFsQ29tbW9uIGZyb20gJ0BzdXBlcnNldC11aS9jb2xvci9lc20vY29sb3JTY2hlbWVzL3NlcXVlbnRpYWwvY29tbW9uJztcbmltcG9ydCBzZXF1ZW50aWFsRDMgZnJvbSAnQHN1cGVyc2V0LXVpL2NvbG9yL2VzbS9jb2xvclNjaGVtZXMvc2VxdWVudGlhbC9kMyc7XG5pbXBvcnQgeyBnZXRDYXRlZ29yaWNhbFNjaGVtZVJlZ2lzdHJ5LCBnZXRTZXF1ZW50aWFsU2NoZW1lUmVnaXN0cnkgfSBmcm9tICdAc3VwZXJzZXQtdWkvY29sb3InO1xuXG5leHBvcnQgZGVmYXVsdCBmdW5jdGlvbiBzZXR1cENvbG9ycygpIHtcbiAgLy8gUmVnaXN0ZXIgY29sb3Igc2NoZW1lc1xuICBjb25zdCBjYXRlZ29yaWNhbFNjaGVtZVJlZ2lzdHJ5ID0gZ2V0Q2F0ZWdvcmljYWxTY2hlbWVSZWdpc3RyeSgpO1xuICBbYWlyYm5iLCBjYXRlZ29yaWNhbEQzLCBnb29nbGUsIGx5ZnRdLmZvckVhY2goKGdyb3VwKSA9PiB7XG4gICAgZ3JvdXAuZm9yRWFjaCgoc2NoZW1lKSA9PiB7XG4gICAgICBjYXRlZ29yaWNhbFNjaGVtZVJlZ2lzdHJ5LnJlZ2lzdGVyVmFsdWUoc2NoZW1lLmlkLCBzY2hlbWUpO1xuICAgIH0pO1xuICB9KTtcbiAgY2F0ZWdvcmljYWxTY2hlbWVSZWdpc3RyeS5zZXREZWZhdWx0S2V5KCdibmJDb2xvcnMnKTtcblxuICBjb25zdCBzZXF1ZW50aWFsU2NoZW1lUmVnaXN0cnkgPSBnZXRTZXF1ZW50aWFsU2NoZW1lUmVnaXN0cnkoKTtcbiAgW3NlcXVlbnRpYWxDb21tb24sIHNlcXVlbnRpYWxEM10uZm9yRWFjaCgoZ3JvdXApID0+IHtcbiAgICBncm91cC5mb3JFYWNoKChzY2hlbWUpID0+IHtcbiAgICAgIHNlcXVlbnRpYWxTY2hlbWVSZWdpc3RyeS5yZWdpc3RlclZhbHVlKHNjaGVtZS5pZCwgc2NoZW1lKTtcbiAgICB9KTtcbiAgfSk7XG59XG4iXSwibWFwcGluZ3MiOiI7Ozs7Ozs7Ozs7Ozs7OztBQUFBOzs7Ozs7Ozs7Ozs7Ozs7Ozs7QUFrQkE7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFFQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFFQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTs7Ozs7Ozs7Ozs7O0FBaEJBOzs7OztBIiwic291cmNlUm9vdCI6IiJ9\n//# sourceURL=webpack-internal:///./src/setup/setupColors.js\n");

/***/ }),

/***/ "./src/setup/setupFormatters.js":
/*!**************************************!*\
  !*** ./src/setup/setupFormatters.js ***!
  \**************************************/
/*! exports provided: default */
/***/ (function(module, __webpack_exports__, __webpack_require__) {

"use strict";
eval("__webpack_require__.r(__webpack_exports__);\n/* WEBPACK VAR INJECTION */(function(module) {/* harmony export (binding) */ __webpack_require__.d(__webpack_exports__, \"default\", function() { return setupFormatters; });\n/* harmony import */ var _superset_ui_number_format__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! @superset-ui/number-format */ \"./node_modules/@superset-ui/number-format/esm/index.js\");\n/* harmony import */ var _superset_ui_time_format__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(/*! @superset-ui/time-format */ \"./node_modules/@superset-ui/time-format/esm/index.js\");\n(function () {\n  var enterModule = __webpack_require__(/*! react-hot-loader */ \"./node_modules/react-hot-loader/index.js\").enterModule;\n\n  enterModule && enterModule(module);\n})();\n\n/**\n * Licensed to the Apache Software Foundation (ASF) under one\n * or more contributor license agreements.  See the NOTICE file\n * distributed with this work for additional information\n * regarding copyright ownership.  The ASF licenses this file\n * to you under the Apache License, Version 2.0 (the\n * \"License\"); you may not use this file except in compliance\n * with the License.  You may obtain a copy of the License at\n *\n *   http://www.apache.org/licenses/LICENSE-2.0\n *\n * Unless required by applicable law or agreed to in writing,\n * software distributed under the License is distributed on an\n * \"AS IS\" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY\n * KIND, either express or implied.  See the License for the\n * specific language governing permissions and limitations\n * under the License.\n */\n\n\nfunction setupFormatters() {\n  var defaultNumberFormatter = Object(_superset_ui_number_format__WEBPACK_IMPORTED_MODULE_0__[\"createSiAtMostNDigitFormatter\"])({\n    n: 3\n  });\n  Object(_superset_ui_number_format__WEBPACK_IMPORTED_MODULE_0__[\"getNumberFormatterRegistry\"])().registerValue(defaultNumberFormatter.id, defaultNumberFormatter).setDefaultKey(defaultNumberFormatter.id) // Add shims for format strings that are deprecated or common typos.\n  // Temporary solution until performing a db migration to fix this.\n  .registerValue(',0', Object(_superset_ui_number_format__WEBPACK_IMPORTED_MODULE_0__[\"getNumberFormatter\"])(',.4~f')).registerValue('null', Object(_superset_ui_number_format__WEBPACK_IMPORTED_MODULE_0__[\"getNumberFormatter\"])(',.4~f')).registerValue('%', Object(_superset_ui_number_format__WEBPACK_IMPORTED_MODULE_0__[\"getNumberFormatter\"])('.0%')).registerValue('.', Object(_superset_ui_number_format__WEBPACK_IMPORTED_MODULE_0__[\"getNumberFormatter\"])('.4~f')).registerValue(',f', Object(_superset_ui_number_format__WEBPACK_IMPORTED_MODULE_0__[\"getNumberFormatter\"])(',d')).registerValue(',r', Object(_superset_ui_number_format__WEBPACK_IMPORTED_MODULE_0__[\"getNumberFormatter\"])(',.4f')).registerValue('0f', Object(_superset_ui_number_format__WEBPACK_IMPORTED_MODULE_0__[\"getNumberFormatter\"])(',d')).registerValue(',#', Object(_superset_ui_number_format__WEBPACK_IMPORTED_MODULE_0__[\"getNumberFormatter\"])(',.4~f')).registerValue('$,f', Object(_superset_ui_number_format__WEBPACK_IMPORTED_MODULE_0__[\"getNumberFormatter\"])('$,d')).registerValue('0%', Object(_superset_ui_number_format__WEBPACK_IMPORTED_MODULE_0__[\"getNumberFormatter\"])('.0%')).registerValue('f', Object(_superset_ui_number_format__WEBPACK_IMPORTED_MODULE_0__[\"getNumberFormatter\"])(',d')).registerValue(',.', Object(_superset_ui_number_format__WEBPACK_IMPORTED_MODULE_0__[\"getNumberFormatter\"])(',.4~f')).registerValue('.1%f', Object(_superset_ui_number_format__WEBPACK_IMPORTED_MODULE_0__[\"getNumberFormatter\"])('.1%')).registerValue('1%', Object(_superset_ui_number_format__WEBPACK_IMPORTED_MODULE_0__[\"getNumberFormatter\"])('.0%')).registerValue('3%', Object(_superset_ui_number_format__WEBPACK_IMPORTED_MODULE_0__[\"getNumberFormatter\"])('.0%')).registerValue(',%', Object(_superset_ui_number_format__WEBPACK_IMPORTED_MODULE_0__[\"getNumberFormatter\"])(',.0%')).registerValue('.r', Object(_superset_ui_number_format__WEBPACK_IMPORTED_MODULE_0__[\"getNumberFormatter\"])('.4~f')).registerValue('$,.0', Object(_superset_ui_number_format__WEBPACK_IMPORTED_MODULE_0__[\"getNumberFormatter\"])('$,d')).registerValue('$,.1', Object(_superset_ui_number_format__WEBPACK_IMPORTED_MODULE_0__[\"getNumberFormatter\"])('$,.1~f')).registerValue(',0s', Object(_superset_ui_number_format__WEBPACK_IMPORTED_MODULE_0__[\"getNumberFormatter\"])(',.4~f')).registerValue('%%%', Object(_superset_ui_number_format__WEBPACK_IMPORTED_MODULE_0__[\"getNumberFormatter\"])('.0%')).registerValue(',0f', Object(_superset_ui_number_format__WEBPACK_IMPORTED_MODULE_0__[\"getNumberFormatter\"])(',d')).registerValue('+,%', Object(_superset_ui_number_format__WEBPACK_IMPORTED_MODULE_0__[\"getNumberFormatter\"])('+,.0%')).registerValue('$f', Object(_superset_ui_number_format__WEBPACK_IMPORTED_MODULE_0__[\"getNumberFormatter\"])('$,d')).registerValue('+,', Object(_superset_ui_number_format__WEBPACK_IMPORTED_MODULE_0__[\"getNumberFormatter\"])(_superset_ui_number_format__WEBPACK_IMPORTED_MODULE_0__[\"NumberFormats\"].INTEGER_CHANGE)).registerValue(',2f', Object(_superset_ui_number_format__WEBPACK_IMPORTED_MODULE_0__[\"getNumberFormatter\"])(',.4~f')).registerValue(',g', Object(_superset_ui_number_format__WEBPACK_IMPORTED_MODULE_0__[\"getNumberFormatter\"])(',.4~f')).registerValue('int', Object(_superset_ui_number_format__WEBPACK_IMPORTED_MODULE_0__[\"getNumberFormatter\"])(_superset_ui_number_format__WEBPACK_IMPORTED_MODULE_0__[\"NumberFormats\"].INTEGER)).registerValue('.0%f', Object(_superset_ui_number_format__WEBPACK_IMPORTED_MODULE_0__[\"getNumberFormatter\"])('.1%')).registerValue('$,0', Object(_superset_ui_number_format__WEBPACK_IMPORTED_MODULE_0__[\"getNumberFormatter\"])('$,.4f')).registerValue('$,0f', Object(_superset_ui_number_format__WEBPACK_IMPORTED_MODULE_0__[\"getNumberFormatter\"])('$,.4f')).registerValue('$,.f', Object(_superset_ui_number_format__WEBPACK_IMPORTED_MODULE_0__[\"getNumberFormatter\"])('$,.4f'));\n  Object(_superset_ui_time_format__WEBPACK_IMPORTED_MODULE_1__[\"getTimeFormatterRegistry\"])().registerValue('smart_date', _superset_ui_time_format__WEBPACK_IMPORTED_MODULE_1__[\"smartDateFormatter\"]).registerValue('smart_date_verbose', _superset_ui_time_format__WEBPACK_IMPORTED_MODULE_1__[\"smartDateVerboseFormatter\"]).setDefaultKey('smart_date');\n}\n;\n\n(function () {\n  var reactHotLoader = __webpack_require__(/*! react-hot-loader */ \"./node_modules/react-hot-loader/index.js\").default;\n\n  var leaveModule = __webpack_require__(/*! react-hot-loader */ \"./node_modules/react-hot-loader/index.js\").leaveModule;\n\n  if (!reactHotLoader) {\n    return;\n  }\n\n  reactHotLoader.register(setupFormatters, \"setupFormatters\", \"/home/leonardo/proyectos/dashboard/incubator-superset/superset/assets/src/setup/setupFormatters.js\");\n  leaveModule(module);\n})();\n\n;\n/* WEBPACK VAR INJECTION */}.call(this, __webpack_require__(/*! ./../../node_modules/webpack/buildin/harmony-module.js */ \"./node_modules/webpack/buildin/harmony-module.js\")(module)))//# sourceURL=[module]\n//# sourceMappingURL=data:application/json;charset=utf-8;base64,eyJ2ZXJzaW9uIjozLCJmaWxlIjoiLi9zcmMvc2V0dXAvc2V0dXBGb3JtYXR0ZXJzLmpzLmpzIiwic291cmNlcyI6WyJ3ZWJwYWNrOi8vLy4vc3JjL3NldHVwL3NldHVwRm9ybWF0dGVycy5qcz9hMTdhIl0sInNvdXJjZXNDb250ZW50IjpbIi8qKlxuICogTGljZW5zZWQgdG8gdGhlIEFwYWNoZSBTb2Z0d2FyZSBGb3VuZGF0aW9uIChBU0YpIHVuZGVyIG9uZVxuICogb3IgbW9yZSBjb250cmlidXRvciBsaWNlbnNlIGFncmVlbWVudHMuICBTZWUgdGhlIE5PVElDRSBmaWxlXG4gKiBkaXN0cmlidXRlZCB3aXRoIHRoaXMgd29yayBmb3IgYWRkaXRpb25hbCBpbmZvcm1hdGlvblxuICogcmVnYXJkaW5nIGNvcHlyaWdodCBvd25lcnNoaXAuICBUaGUgQVNGIGxpY2Vuc2VzIHRoaXMgZmlsZVxuICogdG8geW91IHVuZGVyIHRoZSBBcGFjaGUgTGljZW5zZSwgVmVyc2lvbiAyLjAgKHRoZVxuICogXCJMaWNlbnNlXCIpOyB5b3UgbWF5IG5vdCB1c2UgdGhpcyBmaWxlIGV4Y2VwdCBpbiBjb21wbGlhbmNlXG4gKiB3aXRoIHRoZSBMaWNlbnNlLiAgWW91IG1heSBvYnRhaW4gYSBjb3B5IG9mIHRoZSBMaWNlbnNlIGF0XG4gKlxuICogICBodHRwOi8vd3d3LmFwYWNoZS5vcmcvbGljZW5zZXMvTElDRU5TRS0yLjBcbiAqXG4gKiBVbmxlc3MgcmVxdWlyZWQgYnkgYXBwbGljYWJsZSBsYXcgb3IgYWdyZWVkIHRvIGluIHdyaXRpbmcsXG4gKiBzb2Z0d2FyZSBkaXN0cmlidXRlZCB1bmRlciB0aGUgTGljZW5zZSBpcyBkaXN0cmlidXRlZCBvbiBhblxuICogXCJBUyBJU1wiIEJBU0lTLCBXSVRIT1VUIFdBUlJBTlRJRVMgT1IgQ09ORElUSU9OUyBPRiBBTllcbiAqIEtJTkQsIGVpdGhlciBleHByZXNzIG9yIGltcGxpZWQuICBTZWUgdGhlIExpY2Vuc2UgZm9yIHRoZVxuICogc3BlY2lmaWMgbGFuZ3VhZ2UgZ292ZXJuaW5nIHBlcm1pc3Npb25zIGFuZCBsaW1pdGF0aW9uc1xuICogdW5kZXIgdGhlIExpY2Vuc2UuXG4gKi9cbmltcG9ydCB7IGdldE51bWJlckZvcm1hdHRlciwgZ2V0TnVtYmVyRm9ybWF0dGVyUmVnaXN0cnksIGNyZWF0ZVNpQXRNb3N0TkRpZ2l0Rm9ybWF0dGVyLCBOdW1iZXJGb3JtYXRzIH0gZnJvbSAnQHN1cGVyc2V0LXVpL251bWJlci1mb3JtYXQnO1xuaW1wb3J0IHsgZ2V0VGltZUZvcm1hdHRlclJlZ2lzdHJ5LCBzbWFydERhdGVGb3JtYXR0ZXIsIHNtYXJ0RGF0ZVZlcmJvc2VGb3JtYXR0ZXIgfSBmcm9tICdAc3VwZXJzZXQtdWkvdGltZS1mb3JtYXQnO1xuXG5leHBvcnQgZGVmYXVsdCBmdW5jdGlvbiBzZXR1cEZvcm1hdHRlcnMoKSB7XG4gIGNvbnN0IGRlZmF1bHROdW1iZXJGb3JtYXR0ZXIgPSBjcmVhdGVTaUF0TW9zdE5EaWdpdEZvcm1hdHRlcih7IG46IDMgfSk7XG5cbiAgZ2V0TnVtYmVyRm9ybWF0dGVyUmVnaXN0cnkoKVxuICAgIC5yZWdpc3RlclZhbHVlKGRlZmF1bHROdW1iZXJGb3JtYXR0ZXIuaWQsIGRlZmF1bHROdW1iZXJGb3JtYXR0ZXIpXG4gICAgLnNldERlZmF1bHRLZXkoZGVmYXVsdE51bWJlckZvcm1hdHRlci5pZClcbiAgICAvLyBBZGQgc2hpbXMgZm9yIGZvcm1hdCBzdHJpbmdzIHRoYXQgYXJlIGRlcHJlY2F0ZWQgb3IgY29tbW9uIHR5cG9zLlxuICAgIC8vIFRlbXBvcmFyeSBzb2x1dGlvbiB1bnRpbCBwZXJmb3JtaW5nIGEgZGIgbWlncmF0aW9uIHRvIGZpeCB0aGlzLlxuICAgIC5yZWdpc3RlclZhbHVlKCcsMCcsIGdldE51bWJlckZvcm1hdHRlcignLC40fmYnKSlcbiAgICAucmVnaXN0ZXJWYWx1ZSgnbnVsbCcsIGdldE51bWJlckZvcm1hdHRlcignLC40fmYnKSlcbiAgICAucmVnaXN0ZXJWYWx1ZSgnJScsIGdldE51bWJlckZvcm1hdHRlcignLjAlJykpXG4gICAgLnJlZ2lzdGVyVmFsdWUoJy4nLCBnZXROdW1iZXJGb3JtYXR0ZXIoJy40fmYnKSlcbiAgICAucmVnaXN0ZXJWYWx1ZSgnLGYnLCBnZXROdW1iZXJGb3JtYXR0ZXIoJyxkJykpXG4gICAgLnJlZ2lzdGVyVmFsdWUoJyxyJywgZ2V0TnVtYmVyRm9ybWF0dGVyKCcsLjRmJykpXG4gICAgLnJlZ2lzdGVyVmFsdWUoJzBmJywgZ2V0TnVtYmVyRm9ybWF0dGVyKCcsZCcpKVxuICAgIC5yZWdpc3RlclZhbHVlKCcsIycsIGdldE51bWJlckZvcm1hdHRlcignLC40fmYnKSlcbiAgICAucmVnaXN0ZXJWYWx1ZSgnJCxmJywgZ2V0TnVtYmVyRm9ybWF0dGVyKCckLGQnKSlcbiAgICAucmVnaXN0ZXJWYWx1ZSgnMCUnLCBnZXROdW1iZXJGb3JtYXR0ZXIoJy4wJScpKVxuICAgIC5yZWdpc3RlclZhbHVlKCdmJywgZ2V0TnVtYmVyRm9ybWF0dGVyKCcsZCcpKVxuICAgIC5yZWdpc3RlclZhbHVlKCcsLicsIGdldE51bWJlckZvcm1hdHRlcignLC40fmYnKSlcbiAgICAucmVnaXN0ZXJWYWx1ZSgnLjElZicsIGdldE51bWJlckZvcm1hdHRlcignLjElJykpXG4gICAgLnJlZ2lzdGVyVmFsdWUoJzElJywgZ2V0TnVtYmVyRm9ybWF0dGVyKCcuMCUnKSlcbiAgICAucmVnaXN0ZXJWYWx1ZSgnMyUnLCBnZXROdW1iZXJGb3JtYXR0ZXIoJy4wJScpKVxuICAgIC5yZWdpc3RlclZhbHVlKCcsJScsIGdldE51bWJlckZvcm1hdHRlcignLC4wJScpKVxuICAgIC5yZWdpc3RlclZhbHVlKCcucicsIGdldE51bWJlckZvcm1hdHRlcignLjR+ZicpKVxuICAgIC5yZWdpc3RlclZhbHVlKCckLC4wJywgZ2V0TnVtYmVyRm9ybWF0dGVyKCckLGQnKSlcbiAgICAucmVnaXN0ZXJWYWx1ZSgnJCwuMScsIGdldE51bWJlckZvcm1hdHRlcignJCwuMX5mJykpXG4gICAgLnJlZ2lzdGVyVmFsdWUoJywwcycsIGdldE51bWJlckZvcm1hdHRlcignLC40fmYnKSlcbiAgICAucmVnaXN0ZXJWYWx1ZSgnJSUlJywgZ2V0TnVtYmVyRm9ybWF0dGVyKCcuMCUnKSlcbiAgICAucmVnaXN0ZXJWYWx1ZSgnLDBmJywgZ2V0TnVtYmVyRm9ybWF0dGVyKCcsZCcpKVxuICAgIC5yZWdpc3RlclZhbHVlKCcrLCUnLCBnZXROdW1iZXJGb3JtYXR0ZXIoJyssLjAlJykpXG4gICAgLnJlZ2lzdGVyVmFsdWUoJyRmJywgZ2V0TnVtYmVyRm9ybWF0dGVyKCckLGQnKSlcbiAgICAucmVnaXN0ZXJWYWx1ZSgnKywnLCBnZXROdW1iZXJGb3JtYXR0ZXIoTnVtYmVyRm9ybWF0cy5JTlRFR0VSX0NIQU5HRSkpXG4gICAgLnJlZ2lzdGVyVmFsdWUoJywyZicsIGdldE51bWJlckZvcm1hdHRlcignLC40fmYnKSlcbiAgICAucmVnaXN0ZXJWYWx1ZSgnLGcnLCBnZXROdW1iZXJGb3JtYXR0ZXIoJywuNH5mJykpXG4gICAgLnJlZ2lzdGVyVmFsdWUoJ2ludCcsIGdldE51bWJlckZvcm1hdHRlcihOdW1iZXJGb3JtYXRzLklOVEVHRVIpKVxuICAgIC5yZWdpc3RlclZhbHVlKCcuMCVmJywgZ2V0TnVtYmVyRm9ybWF0dGVyKCcuMSUnKSlcbiAgICAucmVnaXN0ZXJWYWx1ZSgnJCwwJywgZ2V0TnVtYmVyRm9ybWF0dGVyKCckLC40ZicpKVxuICAgIC5yZWdpc3RlclZhbHVlKCckLDBmJywgZ2V0TnVtYmVyRm9ybWF0dGVyKCckLC40ZicpKVxuICAgIC5yZWdpc3RlclZhbHVlKCckLC5mJywgZ2V0TnVtYmVyRm9ybWF0dGVyKCckLC40ZicpKTtcblxuICBnZXRUaW1lRm9ybWF0dGVyUmVnaXN0cnkoKVxuICAgIC5yZWdpc3RlclZhbHVlKCdzbWFydF9kYXRlJywgc21hcnREYXRlRm9ybWF0dGVyKVxuICAgIC5yZWdpc3RlclZhbHVlKCdzbWFydF9kYXRlX3ZlcmJvc2UnLCBzbWFydERhdGVWZXJib3NlRm9ybWF0dGVyKVxuICAgIC5zZXREZWZhdWx0S2V5KCdzbWFydF9kYXRlJyk7XG59XG4iXSwibWFwcGluZ3MiOiI7Ozs7Ozs7Ozs7QUFBQTs7Ozs7Ozs7Ozs7Ozs7Ozs7O0FBa0JBO0FBQ0E7QUFFQTtBQUNBO0FBQUE7QUFBQTtBQUVBO0FBSUE7QUFKQTtBQXNDQTtBQUlBOzs7Ozs7Ozs7Ozs7QUE3Q0E7Ozs7O0EiLCJzb3VyY2VSb290IjoiIn0=\n//# sourceURL=webpack-internal:///./src/setup/setupFormatters.js\n");

/***/ }),

/***/ 0:
/*!**********************************************!*\
  !*** multi babel-polyfill ./src/preamble.js ***!
  \**********************************************/
/*! no static exports found */
/***/ (function(module, exports, __webpack_require__) {

__webpack_require__(/*! babel-polyfill */"./node_modules/babel-polyfill/lib/index.js");
module.exports = __webpack_require__(/*! /home/leonardo/proyectos/dashboard/incubator-superset/superset/assets/src/preamble.js */"./src/preamble.js");


/***/ })

/******/ });