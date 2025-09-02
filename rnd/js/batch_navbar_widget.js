// =============================================================================
// BATCH NAVBAR WIDGET - Fixed Role Detection Version
// =============================================================================

frappe.provide('frappe.ui');
frappe.provide('rnd.batch_widget');

// Initialize when document is ready
$(document).ready(function() {
    setTimeout(initializeBatchWidget, 3000);
});

function initializeBatchWidget() {
    if (typeof frappe === 'undefined' || !frappe.session || frappe.session.user === 'Guest') {
        setTimeout(initializeBatchWidget, 1000);
        return;
    }

    console.log('🚀 Initializing Batch Navbar Widget for user:', frappe.session.user);
    addWidgetStyles();
    
    setInterval(update_batch_announcements, 30000);
    setTimeout(update_batch_announcements, 2000);
}

function update_batch_announcements() {
    console.log('🔄 Fetching Batch AMB data for user:', frappe.session.user);
    
    // Wait for user roles to load
    waitForUserRoles().then(() => {
        const userFilters = getUserSpecificFilters();
        console.log('👤 User roles loaded:', frappe.session.user_roles);
        console.log('🔍 Using filters:', userFilters);
        
        frappe.call({
            method: 'frappe.client.get_list',
            args: {
                doctype: 'Batch AMB',
                fields: ['name', 'title', 'wo_start_date', 'status', 'custom_batch_level', 'production_plant_name', 'operator'],
                filters: userFilters,
                limit: 15,
                order_by: 'modified desc'
            },
            callback: function(r) {
                if (r.message && r.message.length > 0) {
                    console.log('✅ Found', r.message.length, 'active batches for', frappe.session.user);
                    process_batch_data(r.message);
                } else {
                    console.log('ℹ️ No active batches found for', frappe.session.user);
                    show_no_batches_message();
                }
            },
            error: function(r) {
                console.log('⚠️ No batches found or connection issue for', frappe.session.user);
                show_no_batches_message();
            }
        });
    });
}

function waitForUserRoles() {
    return new Promise((resolve) => {
        if (frappe.session.user_roles && frappe.session.user_roles.length > 0) {
            resolve();
        } else {
            // Wait for roles to load
            const checkRoles = setInterval(() => {
                if (frappe.session.user_roles && frappe.session.user_roles.length > 0) {
                    clearInterval(checkRoles);
                    resolve();
                }
            }, 100);
            
            // Timeout after 5 seconds
            setTimeout(() => {
                clearInterval(checkRoles);
                console.log('⚠️ Roles not loaded, using default filters');
                resolve();
            }, 5000);
        }
    });
}

function getUserSpecificFilters() {
    let baseFilters = { 'status': ['!=', 'Completed'] };
    
    // Check if roles are loaded
    if (!frappe.session.user_roles || frappe.session.user_roles.length === 0) {
        console.log('⚠️ Roles not loaded yet, using default filters');
        return baseFilters;
    }
    
    const userRoles = frappe.session.user_roles;
    const userName = frappe.session.user;
    
    console.log('🎯 User roles detected:', userRoles);
    
    // Role-based filtering
    if (userRoles.includes('Manufacturing Manager') || userRoles.includes('System Manager')) {
        baseFilters.status = ['!=', 'Completed'];
        console.log('👔 Manufacturing Manager detected - showing all batches');
    } 
    else if (userRoles.includes('Manufacturing User')) {
        baseFilters.status = ['in', ['Running', 'In Progress']];
        console.log('🏭 Manufacturing User detected - showing running batches only');
    }
    else if (userRoles.includes('Quality Manager')) {
        baseFilters.status = ['in', ['Quality Check', 'Quality Hold', 'Quality Approval']];
        console.log('✅ Quality Manager detected - showing quality-related batches');
    }
    else if (userRoles.includes('Operator')) {
        baseFilters.status = ['!=', 'Completed'];
        baseFilters.operator = userName;
        console.log('👤 Operator detected - showing only assigned batches');
    }
    else {
        console.log('ℹ️ No specific roles detected, using default filters');
    }
    
    return baseFilters;
}

function process_batch_data(batches) {
    const announcements = batches.map(batch => {
        return {
            id: batch.name,
            title: batch.title || batch.name,
            start_date: batch.wo_start_date,
            status: batch.status || 'Active',
            level: batch.custom_batch_level || '1',
            plant: batch.production_plant_name,
            operator: batch.operator
        };
    });
    
    display_batch_announcements(announcements);
}

function display_batch_announcements(announcements) {
    let announcement_html = '';
    
    announcements.forEach(function(announcement, index) {
        const levelColors = {'1': '#e74c3c', '2': '#3498db', '3': '#2ecc71', '4': '#f39c12'};
        const color = levelColors[announcement.level] || '#95a5a6';
        
        announcement_html += `
            <div class="batch-announcement-item" data-batch-id="${announcement.id}" 
                 style="margin-bottom: 12px; padding: 12px; background: white; 
                        color: #333; border-radius: 8px; border-left: 4px solid ${color};
                        position: relative; cursor: pointer; box-shadow: 0 2px 8px rgba(0,0,0,0.1);
                        transition: all 0.3s ease;">
                
                <div style="font-weight: bold; margin-bottom: 8px; font-size: 14px;">
                    🏭 ${announcement.title}
                </div>
                
                <div style="font-size: 11px; color: #555;">
                    🔢 ID: ${announcement.id}
                </div>
                
                <div style="font-size: 11px; color: #555; margin-top: 4px;">
                    📊 Nivel: ${announcement.level} • Estado: <strong>${announcement.status}</strong>
                </div>
                
                ${announcement.plant ? `
                <div style="font-size: 11px; color: #555; margin-top: 4px;">
                    📍 Planta: ${announcement.plant}
                </div>
                ` : ''}
                
                ${announcement.operator ? `
                <div style="font-size: 11px; color: #555; margin-top: 4px;">
                    👤 Operador: ${announcement.operator}
                </div>
                ` : ''}
                
                ${announcement.start_date ? `
                <div style="font-size: 11px; color: #555; margin-top: 4px;">
                    📅 Inicio: ${frappe.datetime.str_to_user(announcement.start_date)}
                </div>
                ` : ''}
                
                <div style="display: flex; justify-content: space-between; align-items: center; margin-top: 8px; font-size: 10px; color: #888;">
                    <span>${new Date().toLocaleTimeString('es-ES')}</span>
                    <span style="background: #28a745; color: white; padding: 2px 6px; border-radius: 3px; font-weight: bold;">
                        ACTIVO
                    </span>
                </div>
            </div>
        `;
    });
    
    show_navbar_widget(announcement_html, announcements.length);
}

function show_navbar_widget(html_content, count) {
    $('.batch-announcement-widget').remove();
    
    const timestamp = new Date().toLocaleTimeString('es-ES');
    const userInfo = frappe.session.user_fullname ? 
        ` • Usuario: ${frappe.session.user_fullname}` : '';

    let widget = $(`
        <div class="batch-announcement-widget" style="position: fixed; top: 70px; right: 20px; width: 450px; max-height: 75vh; overflow-y: auto; 
            z-index: 9999; background: white; color: #333; border: 2px solid #28a745; 
            border-radius: 12px; box-shadow: 0 8px 32px rgba(0,0,0,0.2); padding: 20px;
            animation: slideInRight 0.5s ease-out;">
            
            <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 20px; padding-bottom: 15px; border-bottom: 2px solid #eee;">
                <div>
                    <h4 style="margin: 0; color: #28a745; font-size: 18px; font-weight: 600;">
                        🏭 MONITOR BATCH AMB
                    </h4>
                    <small style="color: #666; font-size: 12px;">
                        ${count} lote${count !== 1 ? 's' : ''} activo${count !== 1 ? 's' : ''}${userInfo} • Actualizado: ${timestamp}
                    </small>
                </div>
                <div style="display: flex; gap: 6px;">
                    <button class="refresh-announcements" style="background: #28a745; border: 1px solid #28a745; color: white; padding: 4px 8px; border-radius: 3px; cursor: pointer; font-size: 12px;" title="Actualizar ahora">
                        🔄
                    </button>
                    <button class="minimize-widget" style="background: #ffc107; border: 1px solid #ffc107; color: white; padding: 4px 8px; border-radius: 3px; cursor: pointer; font-size: 12px;" title="Minimizar">
                        📌
                    </button>
                    <button class="close-announcement" style="background: #dc3545; border: 1px solid #dc3545; color: white; padding: 4px 8px; border-radius: 3px; cursor: pointer; font-size: 12px;" title="Cerrar">
                        ✕
                    </button>
                </div>
            </div>
            
            <div class="announcement-content" style="max-height: 400px; overflow-y: auto; padding-right: 5px;">
                ${html_content || '<div style="text-align: center; padding: 20px; color: #666;">No hay lotes activos en este momento</div>'}
            </div>
            
            <div style="text-align: center; margin-top: 20px; padding-top: 15px; border-top: 1px solid #eee; font-size: 11px; color: #888;">
                <div style="display: flex; justify-content: space-around; margin-bottom: 5px;">
                    <span>🔄 Auto 30s</span>
                    <span>📊 Tiempo real</span>
                    <span>👤 ${frappe.session.user}</span>
                </div>
                <div>
                    <button class="open-batch-list" style="background: #f8f9fa; border: 1px solid #dee2e6; color: #495057; padding: 3px 10px; border-radius: 3px; cursor: pointer; font-size: 10px;" title="Ver todos los batches">
                        📋 Ver lista completa
                    </button>
                </div>
            </div>
        </div>
    `);
    
    $('body').append(widget);
    
    // Add event handlers
    widget.find('.refresh-announcements').click(function() {
        const $btn = $(this);
        $btn.html('⏳').prop('disabled', true);
        update_batch_announcements();
        setTimeout(() => $btn.html('🔄').prop('disabled', false), 1500);
    });
    
    widget.find('.minimize-widget').click(function() {
        widget.toggleClass('minimized');
        if (widget.hasClass('minimized')) {
            widget.css({'width': '60px', 'height': '60px', 'overflow': 'hidden'});
            widget.find('.announcement-content, h4, small, .open-batch-list').hide();
            $(this).html('📋').attr('title', 'Expandir');
        } else {
            widget.css({'width': '450px', 'height': 'auto', 'overflow': 'auto'});
            widget.find('.announcement-content, h4, small, .open-batch-list').show();
            $(this).html('📌').attr('title', 'Minimizar');
        }
    });
    
    widget.find('.close-announcement').click(function() {
        widget.fadeOut(300, function() { $(this).remove(); });
    });
    
    widget.find('.open-batch-list').click(function() {
        frappe.set_route('List', 'Batch AMB', 'List');
    });
    
    widget.find('.batch-announcement-item').click(function() {
        const batchId = $(this).data('batch-id');
        frappe.set_route('Form', 'Batch AMB', batchId);
    });
}

function show_no_batches_message() {
    const userRoles = frappe.session.user_roles ? frappe.session.user_roles.join(', ') : 'No roles';
    const message = `
        <div style="text-align: center; padding: 40px 20px; color: #666;">
            <div style="font-size: 48px; margin-bottom: 15px;">📋</div>
            <h4 style="color: #666; margin-bottom: 10px; font-weight: normal;">No hay lotes activos</h4>
            <p style="font-size: 12px; opacity: 0.7;">Todos los batches están completos o en pausa</p>
            <div style="margin-top: 15px; font-size: 10px; color: #999;">
                Usuario: ${frappe.session.user}<br>
                Roles: ${userRoles}
            </div>
        </div>
    `;
    show_navbar_widget(message, 0);
}

function addWidgetStyles() {
    if ($('#batch-widget-styles').length) return;
    
    const styles = `
        <style id="batch-widget-styles">
            @keyframes slideInRight {
                from { transform: translateX(100%); opacity: 0; }
                to { transform: translateX(0); opacity: 1; }
            }
            
            .batch-announcement-widget {
                transition: all 0.3s ease;
            }
            
            .batch-announcement-item {
                transition: all 0.3s ease;
            }
            
            .batch-announcement-item:hover {
                transform: translateX(-4px);
                box-shadow: 0 4px 15px rgba(0,0,0,0.15);
            }
            
            .refresh-announcements:hover {
                background: #218838 !important;
                border-color: #1e7e34 !important;
            }
            
            .minimize-widget:hover {
                background: #e0a800 !important;
                border-color: #d39e00 !important;
            }
            
            .close-announcement:hover {
                background: #c82333 !important;
                border-color: #bd2130 !important;
            }
            
            .open-batch-list:hover {
                background: #e2e6ea !important;
                border-color: #dae0e5 !important;
            }
            
            @media (max-width: 768px) {
                .batch-announcement-widget {
                    width: calc(100vw - 40px) !important;
                    right: 20px !important;
                    left: 20px !important;
                    top: 80px !important;
                    font-size: 14px !important;
                }
                
                .batch-announcement-widget.minimized {
                    width: 50px !important;
                    height: 50px !important;
                }
            }
        </style>
    `;
    
    $('head').append(styles);
}

// Global functions for manual control
window.BatchWidget = {
    refresh: update_batch_announcements,
    hide: function() {
        $('.batch-announcement-widget').fadeOut(300, function() { $(this).remove(); });
    },
    show: function() {
        update_batch_announcements();
    },
    getUserInfo: function() {
        return {
            user: frappe.session.user,
            fullname: frappe.session.user_fullname,
            roles: frappe.session.user_roles,
            permissions: frappe.session.user_permissions
        };
    }
};

console.log('✅ Fixed Batch AMB Navbar Widget loaded for:', frappe.session.user);
