const API = 'http://localhost:8000';
let currentType = null;
let editingId = null;

// ── Fetch ──

async function fetchPlayers() {
  try {
    const res = await fetch(`${API}/players`);
    const data = await res.json();
    renderCards('players-grid', data, 'player');
  } catch {
    document.getElementById('players-grid').innerHTML = `
      <div class="empty">
        <div class="empty-icon">⚠</div>
        <h3>Connection Error</h3>
        <p>Make sure the API is running at localhost:8000</p>
      </div>`;
  }
}

async function fetchCoaches() {
  try {
    const res = await fetch(`${API}/coaches`);
    const data = await res.json();
    renderCards('coaches-grid', data, 'coach');
  } catch {
    document.getElementById('coaches-grid').innerHTML = `
      <div class="empty">
        <div class="empty-icon">⚠</div>
        <h3>Connection Error</h3>
        <p>Make sure the API is running at localhost:8000</p>
      </div>`;
  }
}

// ── Render ──

function renderCards(containerId, items, type) {
  const container = document.getElementById(containerId);

  if (!items.length) {
    container.innerHTML = `
      <div class="empty">
        <div class="empty-icon">◈</div>
        <h3>No ${type}s registered</h3>
        <p>Register the first ${type} using the button above.</p>
      </div>`;
    return;
  }

  const idField = type === 'player' ? 'id_player' : 'id_coach';

  container.innerHTML = items.map(item => `
    <div class="card">
      <div class="card-header">
        <div style="display:flex; gap:12px; align-items:center">
          <div class="card-avatar">${item.nickname[0].toUpperCase()}</div>
          <div>
            <div class="card-nickname">${item.nickname}</div>
            <div class="card-name">${item.name}</div>
          </div>
        </div>
        <div class="status-dot ${item.active ? '' : 'inactive'}"
             title="${item.active ? 'Looking for team' : 'Inactive'}"></div>
      </div>

      <div class="card-meta">
        ${item.role ? `<span class="badge badge-role">${item.role}</span>` : ''}
        ${item.country ? `<span class="badge badge-country">${item.country}</span>` : ''}
      </div>

      ${item.social ? `<div style="font-size:13px; color:var(--muted); margin-top:4px">🔗 ${item.social}</div>` : ''}
      ${item.birth_date ? `<div style="font-size:12px; color:var(--muted); margin-top:4px">Born: ${item.birth_date}</div>` : ''}

      <div class="card-actions">
        <button class="btn btn-ghost btn-sm" onclick="openEdit('${type}', ${item[idField]})">Edit</button>
        <button class="btn btn-danger btn-sm" onclick="deleteItem('${type}', ${item[idField]})">Delete</button>
      </div>
    </div>
  `).join('');
}

// ── Tabs ──

function switchTab(tab) {
  document.querySelectorAll('.tab').forEach((t, i) => {
    t.classList.toggle('active', (i === 0 && tab === 'players') || (i === 1 && tab === 'coaches'));
  });

  document.querySelectorAll('.section').forEach(s => s.classList.remove('active'));
  document.getElementById(`section-${tab}`).classList.add('active');

  if (tab === 'players') fetchPlayers();
  else fetchCoaches();
}

// ── Modal ──

function openModal(type, data = null) {
  currentType = type;
  editingId = data ? (type === 'player' ? data.id_player : data.id_coach) : null;

  document.getElementById('modal-title').textContent = data ? `Edit ${type}` : `Register ${type}`;

  const roleField = type === 'player' ? `
    <div class="form-group">
      <label>Role</label>
      <select id="f-role">
        <option value="">— select —</option>
        <option value="duelista"    ${data?.role === 'duelista'    ? 'selected' : ''}>Duelista</option>
        <option value="controlador" ${data?.role === 'controlador' ? 'selected' : ''}>Controlador</option>
        <option value="iniciador"   ${data?.role === 'iniciador'   ? 'selected' : ''}>Iniciador</option>
        <option value="sentinela"   ${data?.role === 'sentinela'   ? 'selected' : ''}>Sentinela</option>
        <option value="flex"        ${data?.role === 'flex'        ? 'selected' : ''}>Flex</option>
      </select>
    </div>` : '';

  const activeField = data ? `
    <div class="form-group">
      <label>Status</label>
      <select id="f-active">
        <option value="true"  ${data.active  ? 'selected' : ''}>Looking for team</option>
        <option value="false" ${!data.active ? 'selected' : ''}>Inactive</option>
      </select>
    </div>` : '';

  document.getElementById('modal-form').innerHTML = `
    <div class="form-row">
      <div class="form-group">
        <label>Name *</label>
        <input id="f-name" placeholder="Full name" value="${data?.name || ''}">
      </div>
      <div class="form-group">
        <label>Nickname *</label>
        <input id="f-nickname" placeholder="In-game name" value="${data?.nickname || ''}">
      </div>
    </div>
    <div class="form-row">
      <div class="form-group">
        <label>Country *</label>
        <input id="f-country" placeholder="BR, US, SE..." value="${data?.country || ''}">
      </div>
      <div class="form-group">
        <label>Birth Date</label>
        <input id="f-birth" type="date" value="${data?.birth_date || ''}">
      </div>
    </div>
    ${roleField}
    <div class="form-group">
      <label>Social / Link</label>
      <input id="f-social" placeholder="twitter.com/..." value="${data?.social || ''}">
    </div>
    ${activeField}
  `;

  document.getElementById('modal-overlay').classList.add('open');
}

function closeModal() {
  document.getElementById('modal-overlay').classList.remove('open');
  currentType = null;
  editingId = null;
}

function closeModalOutside(e) {
  if (e.target === document.getElementById('modal-overlay')) closeModal();
}

async function openEdit(type, id) {
  const plural = type === 'coach' ? 'coaches' : 'players';
  const res = await fetch(`${API}/${plural}/${id}`);
  const data = await res.json();
  openModal(type, data);
}

// ── Submit ──

async function submitForm() {
  const name     = document.getElementById('f-name')?.value.trim();
  const nickname = document.getElementById('f-nickname')?.value.trim();
  const country  = document.getElementById('f-country')?.value.trim();

  if (!name || !nickname || !country) {
    showToast('Fill in the required fields.', 'error');
    return;
  }

  const body = { name, nickname, country };

  const role   = document.getElementById('f-role')?.value;
  const birth  = document.getElementById('f-birth')?.value;
  const social = document.getElementById('f-social')?.value.trim();
  const active = document.getElementById('f-active')?.value;

  if (role)   body.role       = role;
  if (birth)  body.birth_date = birth;
  if (social) body.social     = social;
  if (active !== undefined && active !== null) body.active = active === 'true';

  try {
    const typePlural = currentType === 'coach' ? 'coaches' : 'players'; 
    const url    = editingId ? `${API}/${typePlural}/${editingId}` : `${API}/${typePlural}`;
    const method = editingId ? 'PATCH' : 'POST';

    const res = await fetch(url, {
      method,
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(body),
    });

    if (!res.ok) throw new Error();

    showToast(editingId ? 'Updated successfully!' : 'Registered successfully!', 'success');
    closeModal();

    if (currentType === 'player') fetchPlayers();
    else fetchCoaches();

  } catch {
    showToast('Error communicating with the API.', 'error');
  }
}

// ── Delete ──

async function deleteItem(type, id) {
  if (!confirm(`Delete this ${type}?`)) return;

  try {
    const plural = type === 'coach' ? 'coaches' : 'players'; 
    await fetch(`${API}/${plural}/${id}`, { method: 'DELETE' });
    showToast('Deleted successfully!', 'success');
    if (type === 'player') fetchPlayers();
    else fetchCoaches();
  } catch {
    showToast('Error deleting.', 'error');
  }
}

// ── Toast ──

function showToast(msg, type = '') {
  const t = document.getElementById('toast');
  t.textContent = msg;
  t.className = `toast ${type} show`;
  setTimeout(() => t.classList.remove('show'), 3000);
}

// ── Init ──
fetchPlayers();
