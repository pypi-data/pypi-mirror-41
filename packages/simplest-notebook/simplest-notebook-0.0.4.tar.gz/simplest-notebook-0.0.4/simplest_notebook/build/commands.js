"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
/**
 * The map of command ids used by the notebook.
 */
exports.CmdIds = {
    invoke: 'completer:invoke',
    select: 'completer:select',
    invokeNotebook: 'completer:invoke-notebook',
    selectNotebook: 'completer:select-notebook',
    save: 'notebook:save',
    download: 'notebook:download',
    interrupt: 'notebook:interrupt-kernel',
    restart: 'notebook:restart-kernel',
    switchKernel: 'notebook:switch-kernel',
    runAndAdvance: 'notebook-cells:run-and-advance',
    deleteCell: 'notebook-cells:delete',
    selectAbove: 'notebook-cells:select-above',
    selectBelow: 'notebook-cells:select-below',
    extendAbove: 'notebook-cells:extend-above',
    extendBelow: 'notebook-cells:extend-below',
    editMode: 'notebook:edit-mode',
    merge: 'notebook-cells:merge',
    split: 'notebook-cells:split',
    commandMode: 'notebook:command-mode',
    undo: 'notebook-cells:undo',
    redo: 'notebook-cells:redo'
};
