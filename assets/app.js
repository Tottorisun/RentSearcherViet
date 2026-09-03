(function(){
  "use strict";

  // Two ways this script gets its data. The all-in-one page (vietnam-rent-finder.html)
  // inlines everything right here. The per-city pages (assets/app.js) get a
  // small inline <script> before this one that sets window.PAGE_DATA (that
  // city + kind only), window.PAGE_DEFAULT_LANG and window.PAGE = {city, kind};
  // in that mode city tabs and the kind toggle are links to sibling pages.
  // The DATA assignment below must stay one plain literal statement in the
  // all-in-one page: site_data.load_data() and check_js_undefined_calls()
  // locate the data by that exact shape (and this comment must not spell it
  // out, or the regex matches the comment first). The per-city override is
  // therefore a separate line.
  var DEFAULT_LANG = "ru";
  var DATA = null;
  if (typeof window.PAGE_DEFAULT_LANG !== "undefined") DEFAULT_LANG = window.PAGE_DEFAULT_LANG;
  if (typeof window.PAGE_DATA !== "undefined") DATA = window.PAGE_DATA;
  var PAGE = window.PAGE || null;
  var COUNTS = DATA.COUNTS || null;
  var CITIES = DATA.CITIES;
  var SOURCES = DATA.SOURCES;
  var LISTINGS = DATA.LISTINGS;
  function pageHref(city, kind){ return city + (kind === "commercial" ? "-commercial" : "") + ".html"; }

  var SOURCE_LABEL = {};
  SOURCES.forEach(function(s){ SOURCE_LABEL[s.key] = s; });

  var DAY_OPTIONS = [1,3,7,14];
  var BUDGET_CHIPS = [3,5,10,15];
  var DETAIL_ORDER = ["deposit","electricity","water","internet","managementFee","contract","policy","amenities","notice"];

  // Listing `type` is stored in Russian in the data; this maps it for display.
  // The project covers two kinds of property. Listing `type` stays in Russian
  // in the data; TYPE_EN maps it for display, KIND_TYPES splits it by kind.
  var RESIDENTIAL_TYPES = ["Комната","Студия","Квартира","Дом","Другое"];
  var COMMERCIAL_TYPES  = ["Офис","Торговая площадь","Склад"];
  var TYPE_OPTIONS = RESIDENTIAL_TYPES.concat(COMMERCIAL_TYPES);
  var TYPE_EN = {
    "Комната":"Room","Студия":"Studio","Квартира":"Apartment","Дом":"House","Другое":"Other",
    "Офис":"Office","Торговая площадь":"Retail space","Склад":"Warehouse"
  };
  var COMMERCIAL_SET = {};
  COMMERCIAL_TYPES.forEach(function(t){ COMMERCIAL_SET[t] = true; });
  function kindOf(l){ return COMMERCIAL_SET[l.type] ? "commercial" : "residential"; }

  // The page's own language wins on load. index.html IS the Russian page and
  // en.html IS the English one, each with its own <title>, meta and hreflang,
  // so the URL already states which language the visitor asked for.
  //
  // A stored preference used to override this, and it produced exactly the
  // failure en.html exists to prevent: anyone who had once picked Russian --
  // including on the other page, since both share an origin -- then landed on
  // en.html from an English search and got Russian text. The page looked
  // broken to the half of the audience it was built for, and nothing errored.
  //
  // The toggle still switches instantly and keeps your filters, but the choice
  // is not persisted across a reload: the URL decides. Navigating between the
  // two pages on click would keep the address bar in step, but the Artifact
  // build is a single self-contained file with no en.html beside it, so a
  // link there would 404.
  var lang = (typeof DEFAULT_LANG !== "undefined") ? DEFAULT_LANG : "ru";

  var I18N = {
    ru: {
      h1Title:"Жильё во Вьетнаме",
      kindLabel:"Тип недвижимости", kindResidential:"Жильё", kindCommercial:"Коммерция",
      tagline:"Комнаты, студии, квартиры и коммерческие помещения в Хошимине, Ханое, Дананге и Нячанге — из реальных объявлений, отсортированные по цене.",
      themeGroup:"Тема оформления", themeAuto:"Авто", themeLight:"Светлая", themeDark:"Тёмная",
      cityGroup:"Город",
      searchLabel:"Поиск по описанию", searchPlaceholder:"например: бассейн, метро, вид на море", searchClear:"Очистить поиск",
      budgetLabel:"Бюджет, млн ₫ / мес", from:"от", to:"до", mln:"млн ₫",
      districtLabel:"Район", districtPlaceholder:"Начните вводить название района", districtClear:"Сбросить район",
      complexLabel:"ЖК / жилой комплекс", complexAny:"Любой ЖК", complexCtx:"ЖК",
      postedLabel:"Когда опубликовано", sourcesLabel:"Источники",
      datesLabel:"Даты заезда (Airbnb / Agoda / Trip.com / CozyCozy)",
      datesHint:"Появится, когда подключим посуточные сервисы — там снимают на даты, а не на месяцы.",
      typeLabel:"Тип жилья", sortLabel:"Сортировка",
      sortAsc:"Дешевле", sortDesc:"Дороже", sortNew:"Новые", perM2:"сортировать по цене за м²",
      poiLabel:"Ближе к...", poiNone:"не важно", poiMetro:"🚇 метро", poiSchool:"🎓 школе", poiHospital:"✚ больнице",
      mapTitle:"Карта района", mapNote:"реальные границы районов, OpenStreetMap",
      mapLegendPin:"объявление (положение приблизительное)", mapLegendClick:"клик по району на карте — фильтр по нему",
      poiToggle:"метро / школы / госпитали",
      mapCredit:"Карта и адреса — © участники OpenStreetMap (ODbL). Границы районов актуальны после реформы административного деления 2025 года.",
      mapNoBounds:"нет официальных границ районов — показаны только точки объявлений",
      mapCreditNoBounds:"После реформы 2025 года у Нячанга нет официальных границ на уровне районов, поэтому контуры не показаны — только примерные точки объявлений по районам. Карта — © участники OpenStreetMap (ODbL).",
      mapCreditBounds:"Карта и границы районов — © участники OpenStreetMap (ODbL), границы актуальны после реформы административного деления 2025 года.",
      mapCreditHistoric:"Карта и границы — © участники OpenStreetMap (ODbL). Показаны 12 городских районов Ханоя в границах до реформы 2025 года: именно так район называют арендодатели и агенты, а новые кварталы с теми же именами занимают лишь часть прежней территории.",
      mapUnavailable:"Карта недоступна в этом окне — внешние карты (OpenStreetMap) заблокированы политикой безопасности. Откройте страницу как локальный файл, чтобы увидеть интерактивную карту.",
      favFilter:"Избранное", reset:"Сбросить фильтры",
      emptyTitle:"По этим критериям пока пусто", emptyBody:"Попробуйте увеличить бюджет, выбрать другой район или снять фильтр по сроку публикации.",
      supportTitle:"Поддержать проект",
      supportBody:"Сайт бесплатный и без рекламы. Если он помог вам найти жильё — можно поддержать его развитие переводом USDT.",
      supportNetPrefix:"Сеть:", supportNetWarn:"· отправляйте только USDT в этой сети, иначе перевод потеряется.",
      copy:"Скопировать", copied:"Скопировано ✓", selected:"Выделено — скопируйте",
      close:"Закрыть", prevPhoto:"Предыдущее фото", nextPhoto:"Следующее фото",
      districtsWord:"районов", noDistricts:"Районы не найдены",
      any:"Любой", all:"Все", upTo:"до", soon:"· скоро",
      priceOnRequest:"цена по запросу", perMonth:"₫ / мес", wasPrice:"было",
      openListing:"Открыть объявление →", alsoOn:"Также встречается на:",
      popupView:"Посмотреть →",
      detailsToggle:"Подробнее (депозит, коммуналка, удобства)",
      approxPos:"📍 положение на карте приблизительное",
      addFav:"В избранное",
      anyDistrict:"любой район", anyBudget:"любой бюджет", anyType:"любой тип",
      searchCtx:"поиск", forDays:"за", noAdsYet:"пока нет объявлений", adsShort:"объяв.",
      m2:"м²", thousandPerM2:"тыс ₫/м²", mlnShort:"млн", metres:"м", km:"км",
      detailLabels:{deposit:"Депозит", electricity:"Электричество", water:"Вода", internet:"Интернет/wifi",
        managementFee:"Управление", amenities:"Удобства", policy:"Правила", contract:"Договор", notice:"Важно"},
      stamp:"Данные актуальны на 3 сентября 2026 · объявления старше 14 дней исключены из подборки · перед созвоном с хозяином всегда проверяйте цену и наличие по ссылке на объявление."
    },
    en: {
      h1Title:"Rental housing in Vietnam",
      kindLabel:"Property kind", kindResidential:"Housing", kindCommercial:"Commercial",
      tagline:"Rooms, studios, apartments and commercial space in Ho Chi Minh City, Hanoi, Da Nang and Nha Trang — from real listings, sorted by price.",
      themeGroup:"Colour theme", themeAuto:"Auto", themeLight:"Light", themeDark:"Dark",
      cityGroup:"City",
      searchLabel:"Search descriptions", searchPlaceholder:"e.g. pool, metro, sea view", searchClear:"Clear search",
      budgetLabel:"Budget, million ₫ / month", from:"from", to:"to", mln:"mln ₫",
      districtLabel:"District", districtPlaceholder:"Start typing a district name", districtClear:"Clear district",
      complexLabel:"Residential complex", complexAny:"Any complex", complexCtx:"complex",
      postedLabel:"Posted within", sourcesLabel:"Sources",
      datesLabel:"Check-in dates (Airbnb / Agoda / Trip.com / CozyCozy)",
      datesHint:"Coming when per-night services are added — those are booked by date, not by month.",
      typeLabel:"Property type", sortLabel:"Sort by",
      sortAsc:"Cheaper", sortDesc:"Pricier", sortNew:"Newest", perM2:"sort by price per m²",
      poiLabel:"Closer to...", poiNone:"doesn't matter", poiMetro:"🚇 metro", poiSchool:"🎓 school", poiHospital:"✚ hospital",
      mapTitle:"District map", mapNote:"real district boundaries, OpenStreetMap",
      mapLegendPin:"listing (approximate position)", mapLegendClick:"click a district on the map to filter by it",
      poiToggle:"metro / schools / hospitals",
      mapCredit:"Map and addresses — © OpenStreetMap contributors (ODbL). District boundaries reflect the 2025 administrative reform.",
      mapNoBounds:"no official district boundaries — only listing points are shown",
      mapCreditNoBounds:"After the 2025 reform Nha Trang has no official district-level boundaries, so outlines are not shown — only approximate listing points by district. Map — © OpenStreetMap contributors (ODbL).",
      mapCreditBounds:"Map and district boundaries — © OpenStreetMap contributors (ODbL), boundaries reflect the 2025 administrative reform.",
      mapCreditHistoric:"Map and boundaries — © OpenStreetMap contributors (ODbL). Hanoi is shown as its 12 urban districts as they were before the 2025 reform: that is how landlords and agents still name an area, and the new wards that reuse those names cover only part of the old district.",
      mapUnavailable:"The map is unavailable in this window — external maps (OpenStreetMap) are blocked by the security policy. Open the page as a local file to see the interactive map.",
      favFilter:"Favourites", reset:"Reset filters",
      emptyTitle:"Nothing matches these filters yet", emptyBody:"Try raising the budget, picking another district, or clearing the posted-within filter.",
      supportTitle:"Support the project",
      supportBody:"This site is free and ad-free. If it helped you find a place, you can support it with a USDT transfer.",
      supportNetPrefix:"Network:", supportNetWarn:"· send USDT on this network only, otherwise the transfer is lost.",
      copy:"Copy", copied:"Copied ✓", selected:"Selected — copy it",
      close:"Close", prevPhoto:"Previous photo", nextPhoto:"Next photo",
      districtsWord:"districts", noDistricts:"No districts found",
      any:"Any", all:"All", upTo:"up to", soon:"· soon",
      priceOnRequest:"price on request", perMonth:"₫ / month", wasPrice:"was",
      openListing:"Open listing →", alsoOn:"Also listed on:",
      popupView:"View listing →",
      detailsToggle:"More details (deposit, utilities, amenities)",
      approxPos:"📍 approximate position on the map",
      addFav:"Add to favourites",
      anyDistrict:"any district", anyBudget:"any budget", anyType:"any type",
      searchCtx:"search", forDays:"within", noAdsYet:"no listings yet", adsShort:"listings",
      m2:"m²", thousandPerM2:"k ₫/m²", mlnShort:"mln", metres:"m", km:"km",
      detailLabels:{deposit:"Deposit", electricity:"Electricity", water:"Water", internet:"Internet/wifi",
        managementFee:"Management fee", amenities:"Amenities", policy:"House rules", contract:"Contract", notice:"Important"},
      stamp:"Data current as of 3 September 2026 · listings older than 14 days are excluded · always confirm price and availability via the original listing before calling the owner."
    }
  };

  function t(key){ return (I18N[lang] && I18N[lang][key] !== undefined) ? I18N[lang][key] : I18N.ru[key]; }
  // Russian uses a decimal comma, English a decimal point.
  function decSep(s){ return lang === "en" ? s : s.replace(".", ","); }

  function applyLang(next){
    lang = next;
    document.documentElement.setAttribute("lang", lang);
    var lt = document.getElementById("lang-toggle");
    if (lt){
      Array.prototype.forEach.call(lt.querySelectorAll("button"), function(b){
        b.classList.toggle("active", b.getAttribute("data-lang") === lang);
      });
    }
    Array.prototype.forEach.call(document.querySelectorAll("[data-i18n]"), function(node){
      var key = node.getAttribute("data-i18n");
      node.textContent = t(key);
    });
    Array.prototype.forEach.call(document.querySelectorAll("[data-i18n-ph]"), function(node){
      node.setAttribute("placeholder", t(node.getAttribute("data-i18n-ph")));
    });
    Array.prototype.forEach.call(document.querySelectorAll("[data-i18n-aria]"), function(node){
      node.setAttribute("aria-label", t(node.getAttribute("data-i18n-aria")));
    });
    Array.prototype.forEach.call(document.querySelectorAll("[data-i18n-title]"), function(node){
      node.setAttribute("title", t(node.getAttribute("data-i18n-title")));
    });
    // re-render everything that builds its own strings in JS
    renderCityTabs(); renderCityMap(); renderBudgetChips(); renderDaysChips();
    renderSourceChips(); renderTypeChips(); renderComplexFilter(); applyFilters();
    el.favFilterToggle.textContent = (state.showFavoritesOnly ? "★" : "☆") + " " + t("favFilter");
  }

  function initLang(){
    var lt = document.getElementById("lang-toggle");
    if (lt){
      lt.addEventListener("click", function(e){
        var btn = e.target.closest("button[data-lang]");
        if (!btn) return;
        applyLang(btn.getAttribute("data-lang"));
      });
    }
    applyLang(lang);
  }
  function cityName(c){ return (lang === "en" && c.nameEn) ? c.nameEn : c.name; }
  function districtHint(d){ return (lang === "en" && d.hintEn) ? d.hintEn : d.hint; }
  function typeName(tp){ return (lang === "en" && TYPE_EN[tp]) ? TYPE_EN[tp] : tp; }
  // Listings gain an English description over time (the daily checks write
  // descEn for every new listing, and the 14-day purge cycles the whole
  // dataset), so fall back to the Russian text until one exists.
  function descText(l){ return (lang === "en" && l.descEn) ? l.descEn : l.desc; }
  function sourceLabel(s){ return (lang === "en" && s.labelEn) ? s.labelEn : s.label; }
  function noticeText(d){ return (lang === "en" && d.noticeEn) ? d.noticeEn : d.notice; }
  function postedText(l){
    if (lang !== "en") return l.posted;
    if (l.daysAgo === 0) return "today";
    if (l.daysAgo === 1) return "yesterday";
    return l.daysAgo + " days ago";
  }

  var state = {
    city: PAGE ? PAGE.city : "nha-trang", district: null, complex: null, minBudget: null, maxBudget: null, maxDays: 14, sort: "asc", type: null, kind: PAGE ? PAGE.kind : "residential", poiSort: "", textSearch: "", showFavoritesOnly: false, perM2: false,
    sources: new Set(SOURCES.filter(function(s){ return s.active; }).map(function(s){ return s.key; })),
    openDetails: new Set()
  };

  var THEME_KEY = "rentSearcherTheme";
  function applyTheme(choice){
    var root = document.documentElement;
    if (choice === "light" || choice === "dark") root.setAttribute("data-theme", choice);
    else root.removeAttribute("data-theme");
    var toggle = document.getElementById("theme-toggle");
    if (toggle){
      Array.prototype.forEach.call(toggle.querySelectorAll("button"), function(b){
        b.classList.toggle("active", b.getAttribute("data-theme-choice") === choice);
      });
    }
  }
  function initTheme(){
    var saved = "auto";
    try { saved = localStorage.getItem(THEME_KEY) || "auto"; } catch (e) {}
    applyTheme(saved);
    var toggle = document.getElementById("theme-toggle");
    if (toggle){
      toggle.addEventListener("click", function(e){
        var btn = e.target.closest("button[data-theme-choice]");
        if (!btn) return;
        var choice = btn.getAttribute("data-theme-choice");
        applyTheme(choice);
        try { localStorage.setItem(THEME_KEY, choice); } catch (e2) {}
      });
    }
  }

  var FAVORITES_KEY = "rentSearcherFavorites";
  var favorites = (function(){
    try {
      var raw = localStorage.getItem(FAVORITES_KEY);
      return new Set(raw ? JSON.parse(raw) : []);
    } catch (e) { return new Set(); }
  })();
  function saveFavorites(){
    try { localStorage.setItem(FAVORITES_KEY, JSON.stringify(Array.from(favorites))); } catch (e) {}
  }
  function toggleFavorite(id){
    if (favorites.has(id)) favorites.delete(id); else favorites.add(id);
    saveFavorites();
  }

  // Commercial rents reach ~160M VND/month while almost all housing sits under
  // 45M. One shared ceiling cannot serve both: at 45 the commercial listings are
  // invisible, at 300 the residential slider is unusable because everything
  // bunches into its first sixth. So the ceiling follows the selected kind.
  var BUDGET_MIN = 0;
  var BUDGET_MAX_RESIDENTIAL = 45, BUDGET_MAX_COMMERCIAL = 300;
  var BUDGET_MAX = BUDGET_MAX_RESIDENTIAL;

  var el = {
    cityTabs: document.getElementById("city-tabs"),
    textSearchInput: document.getElementById("text-search-input"),
    textSearchClear: document.getElementById("text-search-clear"),
    budgetMinInput: document.getElementById("budget-min-input"),
    budgetMaxInput: document.getElementById("budget-max-input"),
    budgetMinRange: document.getElementById("budget-min-range"),
    budgetMaxRange: document.getElementById("budget-max-range"),
    budgetRangeFill: document.getElementById("budget-range-fill"),
    budgetChips: document.getElementById("budget-chips"),
    districtInput: document.getElementById("district-input"),
    districtClear: document.getElementById("district-clear"),
    districtSuggest: document.getElementById("district-suggest"),
    complexField: document.getElementById("complex-field"),
    complexSelect: document.getElementById("complex-select"),
    daysChips: document.getElementById("days-chips"),
    sourceChips: document.getElementById("source-chips"),
    typeChips: document.getElementById("type-chips"),
    sortToggle: document.getElementById("sort-toggle"),
    perM2Toggle: document.getElementById("per-m2-toggle"),
    poiSortField: document.getElementById("poi-sort-field"),
    poiSortSelect: document.getElementById("poi-sort-select"),
    mapTitle: document.getElementById("map-title"),
    mapSvgWrap: document.getElementById("leaflet-map"),
    resultsCount: document.getElementById("results-count"),
    resultsContext: document.getElementById("results-context"),
    resultsList: document.getElementById("results-list"),
    favFilterToggle: document.getElementById("fav-filter-toggle"),
    emptyState: document.getElementById("empty-state"),
    resetBtn: document.getElementById("reset-filters")
  };

  function fmtPrice(v){
    var m = v/1000000;
    var s = (m % 1 === 0) ? String(m) : decSep(m.toFixed(1));
    return s + " " + t("mlnShort");
  }
  function pricePerM2(l){
    if (l.price == null || !l.area) return null;
    return l.price / l.area;
  }
  function fmtPricePerM2(v){
    return Math.round(v/1000) + " " + t("thousandPerM2");
  }
  function districtByKey(cityKey, distKey){
    var list = CITIES[cityKey].districts;
    for (var i=0;i<list.length;i++){ if (list[i].key===distKey) return list[i]; }
    return null;
  }
  function listingSearchText(l){
    if (l._searchText) return l._searchText;
    var d = districtByKey(l.city, l.district);
    var parts = [l.desc, l.descEn || "", l.type, d ? d.name : "", l.complex || ""];
    if (l.details){
      ["amenities","notice","contract","deposit"].forEach(function(k){ if (l.details[k]) parts.push(l.details[k]); });
    }
    l._searchText = parts.join(" ").toLowerCase();
    return l._searchText;
  }
  function countsForCity(cityKey){
    var counts = {};
    LISTINGS.forEach(function(l){ if (l.city !== cityKey) return; counts[l.district] = (counts[l.district]||0) + 1; });
    return counts;
  }

  // `complex` is filled in at build time (see the COMPLEX_DICT pass in
  // rebuild_final.py) and only a minority of listings carry one, so the whole
  // control hides itself in a city where nothing was detected.
  function complexesForCity(cityKey){
    var counts = {};
    LISTINGS.forEach(function(l){
      if (l.city !== cityKey || !l.complex) return;
      if (l.details && l.details.duplicateOf) return;
      counts[l.complex] = (counts[l.complex]||0) + 1;
    });
    return Object.keys(counts).sort(function(a,b){
      return counts[b]-counts[a] || a.localeCompare(b);
    }).map(function(n){ return {name:n, count:counts[n]}; });
  }

  function renderComplexFilter(){
    var items = complexesForCity(state.city);
    var stillThere = false;
    items.forEach(function(c){ if (c.name === state.complex) stillThere = true; });
    if (state.complex && !stillThere) state.complex = null;
    el.complexField.hidden = (items.length === 0);
    el.complexSelect.innerHTML = "";
    var any = document.createElement("option");
    any.value = ""; any.textContent = t("complexAny");
    el.complexSelect.appendChild(any);
    items.forEach(function(c){
      var o = document.createElement("option");
      o.value = c.name; o.textContent = c.name + " (" + c.count + ")";
      el.complexSelect.appendChild(o);
    });
    el.complexSelect.value = state.complex || "";
  }

  function renderCityTabs(){
    el.cityTabs.innerHTML = "";
    Object.keys(CITIES).forEach(function(key){
      var c = CITIES[key];
      // Per-city pages: the tab is a real link to that city's page for the
      // same kind, with the listing count for the kind. All-in-one page: a
      // button that switches in place, with the district count as before.
      var n = COUNTS && COUNTS[key] ? (COUNTS[key][state.kind] || 0) : null;
      var sub = (n !== null) ? (n + " " + t("adsShort")) : (c.districts.length + " " + t("districtsWord"));
      var btn;
      if (PAGE){
        btn = document.createElement("a");
        btn.href = pageHref(key, state.kind);
      } else {
        btn = document.createElement("button");
        btn.type = "button";
        btn.addEventListener("click", function(){ selectCity(key); });
      }
      btn.className = "city-tab"; btn.setAttribute("role","tab");
      btn.setAttribute("aria-selected", state.city===key ? "true":"false");
      if (PAGE && n === 0) btn.classList.add("empty");
      btn.innerHTML = cityName(c) + '<span class="sub">' + sub + "</span>";
      el.cityTabs.appendChild(btn);
    });
  }

  function selectCity(key){
    if (PAGE){ location.href = pageHref(key, state.kind); return; }
    state.city = key; state.district = null; state.complex = null; el.districtInput.value = "";
    renderCityTabs(); renderCityMap(); updatePoiSortAvailability(); renderComplexFilter(); applyFilters();
  }

  var WARD_BOUNDARIES = DATA.WARD_BOUNDARIES || {};
  var POIS = DATA.POIS || {};
  var POI_STYLE = {
    metro: {bg:"#1E6FBF", icon:"🚇"},
    school: {bg:"#7A3FA0", icon:"🎓"},
    hospital: {bg:"#B44430", icon:"✚"}
  };
  var leafletMap = null, wardLayerGroup = null, markerLayerGroup = null, poiLayerGroup = null, leafletReady = false;
  var wardLayerByKey = {};
  var showPois = false;

  function haversineKm(lat1, lon1, lat2, lon2){
    var R = 6371;
    var dLat = (lat2-lat1) * Math.PI/180;
    var dLon = (lon2-lon1) * Math.PI/180;
    var a = Math.sin(dLat/2)*Math.sin(dLat/2) +
      Math.cos(lat1*Math.PI/180)*Math.cos(lat2*Math.PI/180)*Math.sin(dLon/2)*Math.sin(dLon/2);
    return R * 2 * Math.atan2(Math.sqrt(a), Math.sqrt(1-a));
  }

  function nearestPoiKm(l, poiType){
    var list = POIS[l.city];
    if (!list || l.lat == null || l.lon == null) return null;
    var best = null;
    list.forEach(function(p){
      if (p.type !== poiType) return;
      var km = haversineKm(l.lat, l.lon, p.lat, p.lon);
      if (best === null || km < best) best = km;
    });
    return best;
  }

  function fmtDist(km){
    if (km < 1) return Math.round(km*1000) + " " + t("metres");
    return decSep(km.toFixed(1)) + " " + t("km");
  }

  function updatePoiSortAvailability(){
    var list = POIS[state.city] || [];
    var typesPresent = new Set(list.map(function(p){ return p.type; }));
    var hasPois = list.length > 0;
    el.poiSortField.hidden = !hasPois;
    Array.prototype.forEach.call(el.poiSortSelect.querySelectorAll("option[value]"), function(opt){
      if (opt.value === "") return;
      opt.hidden = !typesPresent.has(opt.value);
    });
    if (state.poiSort && !typesPresent.has(state.poiSort)){
      state.poiSort = "";
      el.poiSortSelect.value = "";
    }
  }

  function initLeafletMap(){
    if (leafletMap || typeof L === "undefined") return;
    leafletMap = L.map("leaflet-map", {scrollWheelZoom:true});
    L.tileLayer("https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png", {
      maxZoom: 19,
      attribution: '&copy; <a href="https://www.openstreetmap.org/copyright" target="_blank" rel="noopener">OpenStreetMap</a> contributors'
    }).addTo(leafletMap);
    wardLayerGroup = L.layerGroup().addTo(leafletMap);
    markerLayerGroup = L.layerGroup().addTo(leafletMap);
    poiLayerGroup = L.layerGroup().addTo(leafletMap);
    leafletReady = true;
    var poiToggle = document.getElementById("poi-toggle");
    if (poiToggle){
      poiToggle.addEventListener("change", function(){
        showPois = poiToggle.checked;
        renderPois(state.city);
      });
    }
  }

  function renderPois(cityKey){
    if (!leafletReady) return;
    poiLayerGroup.clearLayers();
    if (!showPois) return;
    var list = POIS[cityKey];
    if (!list) return;
    list.forEach(function(p){
      var style = POI_STYLE[p.type] || {bg:"#666", icon:"•"};
      var icon = L.divIcon({
        className: "",
        html: '<div class="poi-marker" style="background:'+style.bg+';width:22px;height:22px;">'+style.icon+'</div>',
        iconSize: [22,22], iconAnchor: [11,11]
      });
      L.marker([p.lat, p.lon], {icon: icon}).bindTooltip(p.name).addTo(poiLayerGroup);
    });
  }

  function wardStyle(cnt, selected){
    if (selected) return {color:"var(--accent)", weight:3, fillColor:"#1E7A4C", fillOpacity:0.35};
    if (cnt>0) return {color:"#7C8A6E", weight:1.5, fillColor:"#7C8A6E", fillOpacity:0.14};
    return {color:"#9AA48C", weight:1, fillColor:"#9AA48C", fillOpacity:0.05, dashArray:"3,4"};
  }

  function activateDistrict(key, name){
    state.district = (state.district===key) ? null : key;
    el.districtInput.value = state.district ? name : "";
    renderCityMap(); applyFilters();
  }

  function renderCityMap(){
    var city = CITIES[state.city];
    el.mapTitle.textContent = t("mapTitle") + " — " + cityName(city);
    var noteEl = document.getElementById("map-note");
    var creditEl = document.getElementById("map-credit");
    var boundaries = WARD_BOUNDARIES[state.city];
    if (!boundaries){
      noteEl.textContent = t("mapNoBounds");
      creditEl.textContent = t("mapCreditNoBounds");
    } else {
      noteEl.textContent = t("mapNote");
      // Hanoi's outlines are the pre-2025 districts on purpose (see build_leaflet_data.py)
      creditEl.textContent = (state.city === "ha-noi") ? t("mapCreditHistoric") : t("mapCreditBounds");
    }
    if (!leafletReady){
      el.mapSvgWrap.innerHTML = '<div style="padding:32px 16px;text-align:center;color:var(--ink-dim);font-size:0.88rem;">' + t("mapUnavailable") + '</div>';
      return;
    }
    wardLayerGroup.clearLayers();
    wardLayerByKey = {};
    var counts = countsForCity(state.city);
    var boundsLayers = [];
    if (boundaries){
      city.districts.forEach(function(d){
        var w = boundaries[d.key];
        if (!w) return;
        var cnt = counts[d.key] || 0;
        var poly = L.polygon(w.rings, wardStyle(cnt, state.district===d.key));
        poly.bindTooltip(d.name + (cnt ? (" — " + cnt + " " + t("adsShort")) : (" — " + t("noAdsYet"))));
        poly.on("click", function(){ activateDistrict(d.key, d.name); });
        poly.addTo(wardLayerGroup);
        wardLayerByKey[d.key] = poly;
        boundsLayers.push(poly);
      });
    }
    renderPois(state.city);
    if (boundsLayers.length){
      leafletMap.fitBounds(L.featureGroup(boundsLayers).getBounds(), {padding:[12,12]});
    } else {
      var pts = LISTINGS.filter(function(l){ return l.city===state.city && typeof l.lat==="number"; });
      if (pts.length){
        var b = L.latLngBounds(pts.map(function(l){ return [l.lat, l.lon]; }));
        leafletMap.fitBounds(b, {padding:[24,24]});
      } else {
        leafletMap.setView([16.0,108.0], 6);
      }
    }
  }

  function popupHtml(l){
    var d = districtByKey(l.city, l.district);
    var src = SOURCE_LABEL[l.source];
    var dsc = descText(l);
    var desc = dsc.length > 100 ? dsc.slice(0,100) + "…" : dsc;
    var priceHtml = (l.price===null) ? t("priceOnRequest") : (fmtPrice(l.price) + ' ₫');
    return '<div class="pt-top"><span class="pt-src">' + src.short + '</span><span class="pt-price">' + priceHtml + '</span></div>' +
      '<div class="pt-meta">' + typeName(l.type) + ' · ' + d.name + (l.area ? (" · " + l.area + " " + t("m2")) : "") + '</div>' +
      '<div class="pt-desc">' + desc + '</div>' +
      '<div class="pt-approx">' + t("approxPos") + '</div>' +
      '<a class="pt-view" href="' + l.url + '" target="_blank" rel="noopener">' + t("popupView") + '</a>';
  }

  // Listings that share one coordinate -- every ward-centroid fallback in a
  // district, or several units in one building -- used to stack on a single
  // pixel: only the top marker was clickable and the other 75 (the worst
  // HCMC case) were unreachable. Spread each such group on a sunflower
  // spiral a few metres across; stable per id, so pins don't jump between
  // renders. Precisely-geocoded singletons are left exactly where they are.
  function spreadStackedPins(list){
    var groups = {};
    list.forEach(function(l){
      if (typeof l.lat !== "number" || typeof l.lon !== "number") return;
      var key = l.lat.toFixed(5) + "," + l.lon.toFixed(5);
      (groups[key] = groups[key] || []).push(l);
    });
    var pos = {};
    Object.keys(groups).forEach(function(key){
      var g = groups[key];
      if (g.length === 1){ pos[g[0].id] = [g[0].lat, g[0].lon]; return; }
      g.sort(function(a, b){ return a.id - b.id; });
      var lat0 = g[0].lat, lon0 = g[0].lon;
      var mPerDegLat = 111320, mPerDegLon = 111320 * Math.cos(lat0 * Math.PI / 180);
      var spacing = g.length > 20 ? 7 : 9;                 // metres between neighbours
      g.forEach(function(l, i){
        var r = spacing * Math.sqrt(i + 1), a = i * 2.39996;   // golden angle
        pos[l.id] = [lat0 + (r * Math.sin(a)) / mPerDegLat, lon0 + (r * Math.cos(a)) / mPerDegLon];
      });
    });
    return pos;
  }

  function renderLeafletMarkers(list){
    if (!leafletReady) return;
    markerLayerGroup.clearLayers();
    var pos = spreadStackedPins(list);
    // Fingers are wider than cursors: a 7px dot is hard to hit on a phone.
    var coarsePointer = !!(window.matchMedia && window.matchMedia("(pointer: coarse)").matches);
    var baseRadius = coarsePointer ? 9 : 7;
    list.forEach(function(l){
      if (typeof l.lat !== "number" || typeof l.lon !== "number") return;
      var marker = L.circleMarker(pos[l.id] || [l.lat, l.lon], {
        radius: baseRadius, weight: 1.6, color: "var(--surface)",
        fillColor: "#1E7A4C", fillOpacity: 0.9
      });
      // A tap/click never navigates away: it opens the card and PINS it, so
      // the person can read it; the card's own "Посмотреть" link is the only
      // way to the source. (Before: click = window.open, which on a phone
      // meant every tap on a dot threw you out of the site with no chance to
      // see what it was.) Hover still previews on mouse devices; on touch
      // there is no hover, and emulated mouseout must not close a pinned card
      // before the link inside it can be tapped.
      marker.bindPopup(popupHtml(l), {closeButton:true, maxWidth:240, autoPanPadding:[24,24]});
      marker.off("click");                       // drop Leaflet's open/close toggle
      var pinned = false;
      marker.on("click", function(){ pinned = true; marker.openPopup(); marker.setStyle({radius:10}); });
      marker.on("popupclose", function(){ pinned = false; marker.setStyle({radius: baseRadius}); });
      if (!coarsePointer){
        marker.on("mouseover", function(){ if (!pinned) marker.openPopup(); marker.setStyle({radius:10}); });
        marker.on("mouseout", function(){ if (!pinned){ marker.closePopup(); marker.setStyle({radius: baseRadius}); } });
      }
      marker.addTo(markerLayerGroup);
    });
  }

  function renderSuggestions(){
    var q = el.districtInput.value.trim().toLowerCase();
    var city = CITIES[state.city];
    var matches = city.districts.filter(function(d){
      return !q || d.name.toLowerCase().indexOf(q)!==-1 || districtHint(d).toLowerCase().indexOf(q)!==-1;
    });
    el.districtSuggest.innerHTML = "";
    if (matches.length===0){
      var li = document.createElement("li"); li.className = "suggest-empty"; li.textContent = t("noDistricts");
      el.districtSuggest.appendChild(li);
    } else {
      matches.forEach(function(d){
        var li = document.createElement("li");
        var b = document.createElement("button"); b.type = "button";
        b.innerHTML = "<span>"+d.name+"</span><span class='hint'>"+districtHint(d)+"</span>";
        b.addEventListener("click", function(){
          state.district = d.key; el.districtInput.value = d.name; el.districtSuggest.hidden = true;
          renderCityMap(); applyFilters();
        });
        li.appendChild(b); el.districtSuggest.appendChild(li);
      });
    }
    el.districtSuggest.hidden = false;
  }
  el.districtInput.addEventListener("focus", renderSuggestions);
  el.districtInput.addEventListener("input", function(){
    if (state.district && el.districtInput.value.trim() === "") state.district = null;
    renderSuggestions();
  });
  el.districtInput.addEventListener("keydown", function(e){ if (e.key === "Escape") el.districtSuggest.hidden = true; });
  document.addEventListener("click", function(e){ if (!e.target.closest(".autocomplete")) el.districtSuggest.hidden = true; });
  el.districtClear.addEventListener("click", function(){
    state.district = null; el.districtInput.value = ""; renderCityMap(); applyFilters(); el.districtInput.focus();
  });

  el.textSearchInput.addEventListener("input", function(){
    state.textSearch = el.textSearchInput.value.trim().toLowerCase();
    applyFilters();
  });
  el.textSearchClear.addEventListener("click", function(){
    state.textSearch = ""; el.textSearchInput.value = ""; applyFilters(); el.textSearchInput.focus();
  });

  el.favFilterToggle.addEventListener("click", function(){
    state.showFavoritesOnly = !state.showFavoritesOnly;
    el.favFilterToggle.setAttribute("aria-pressed", state.showFavoritesOnly);
    el.favFilterToggle.textContent = (state.showFavoritesOnly ? "★" : "☆") + " " + t("favFilter");
    applyFilters();
  });

  function renderBudgetChips(){
    el.budgetChips.innerHTML = "";
    var allBtn = document.createElement("button");
    allBtn.type="button"; allBtn.className="chip"; allBtn.textContent=t("any");
    allBtn.setAttribute("aria-pressed", (state.maxBudget===null && state.minBudget===null) ? "true":"false");
    allBtn.addEventListener("click", function(){ setBudgetRange(BUDGET_MIN, BUDGET_MAX); });
    el.budgetChips.appendChild(allBtn);
    BUDGET_CHIPS.forEach(function(v){
      var b = document.createElement("button");
      b.type="button"; b.className="chip"; b.textContent=t("upTo") + " " + v;
      b.setAttribute("aria-pressed", (state.maxBudget===v && state.minBudget===null) ? "true":"false");
      b.addEventListener("click", function(){ setBudgetRange(BUDGET_MIN, v); });
      el.budgetChips.appendChild(b);
    });
  }

  function clampBudget(v){
    if (isNaN(v)) return BUDGET_MIN;
    return Math.max(BUDGET_MIN, Math.min(BUDGET_MAX, v));
  }

  function setBudgetRange(lo, hi, opts){
    lo = clampBudget(lo); hi = clampBudget(hi);
    if (lo > hi){ var t=lo; lo=hi; hi=t; }
    state.minBudget = (lo <= BUDGET_MIN) ? null : lo;
    state.maxBudget = (hi >= BUDGET_MAX) ? null : hi;
    syncBudgetUI(opts);
    renderBudgetChips();
    applyFilters();
  }

  function syncBudgetUI(opts){
    // The bounds live here, not only in setupBudgetSlider: that runs once at
    // init, so when BUDGET_MAX moves (housing 45M -> commercial 300M) the
    // inputs kept the old ceiling and the wider range was unreachable.
    el.budgetMinRange.min = el.budgetMaxRange.min = el.budgetMinInput.min = el.budgetMaxInput.min = BUDGET_MIN;
    el.budgetMinRange.max = el.budgetMaxRange.max = el.budgetMinInput.max = el.budgetMaxInput.max = BUDGET_MAX;
    var lo = state.minBudget===null ? BUDGET_MIN : state.minBudget;
    var hi = state.maxBudget===null ? BUDGET_MAX : state.maxBudget;
    // While the user is typing in one of the number fields, leave BOTH text
    // fields alone: writing the normalised value back on every keystroke made
    // it impossible to clear a field or type "6" over "45" on a phone (the
    // empty field snapped straight back to 0 / 45). The fields are
    // normalised on "change" (blur / Enter) instead. Sliders and the fill
    // bar still follow every keystroke.
    if (!(opts && opts.skipInputs)){
      el.budgetMinInput.value = lo;
      el.budgetMaxInput.value = hi;
    }
    el.budgetMinRange.value = lo;
    el.budgetMaxRange.value = hi;
    var pctLo = (lo - BUDGET_MIN) / (BUDGET_MAX - BUDGET_MIN) * 100;
    var pctHi = (hi - BUDGET_MIN) / (BUDGET_MAX - BUDGET_MIN) * 100;
    el.budgetRangeFill.style.left = pctLo + "%";
    el.budgetRangeFill.style.width = Math.max(0, pctHi - pctLo) + "%";
  }

  function setupBudgetSlider(){
    el.budgetMinRange.min = el.budgetMaxRange.min = el.budgetMinInput.min = el.budgetMaxInput.min = BUDGET_MIN;
    el.budgetMinRange.max = el.budgetMaxRange.max = el.budgetMinInput.max = el.budgetMaxInput.max = BUDGET_MAX;

    el.budgetMinRange.addEventListener("input", function(){
      var lo = parseFloat(el.budgetMinRange.value);
      var hi = state.maxBudget===null ? BUDGET_MAX : state.maxBudget;
      if (lo > hi) lo = hi;
      el.budgetMinRange.classList.add("on-top");
      state.minBudget = (lo <= BUDGET_MIN) ? null : lo;
      syncBudgetUI(); renderBudgetChips(); applyFilters();
    });
    el.budgetMaxRange.addEventListener("input", function(){
      var hi = parseFloat(el.budgetMaxRange.value);
      var lo = state.minBudget===null ? BUDGET_MIN : state.minBudget;
      if (hi < lo) hi = lo;
      el.budgetMinRange.classList.remove("on-top");
      state.maxBudget = (hi >= BUDGET_MAX) ? null : hi;
      syncBudgetUI(); renderBudgetChips(); applyFilters();
    });
    // Typed budget: read what is in the field, never write into it mid-edit.
    // An empty or half-typed field means "no bound for now"; the value is
    // only clamped/ordered in state, and the field itself is tidied on
    // "change" (blur or Enter). Without this, phones could not delete a digit.
    function typedBudget(inp, fallback){
      var raw = inp.value.trim().replace(",", ".");
      if (raw === "" || raw === "." || raw === "-") return fallback;
      var v = parseFloat(raw);
      return isNaN(v) ? fallback : v;
    }
    el.budgetMinInput.addEventListener("input", function(){
      var hi = state.maxBudget===null ? BUDGET_MAX : state.maxBudget;
      var lo = Math.min(typedBudget(el.budgetMinInput, BUDGET_MIN), hi);
      setBudgetRange(lo, hi, {skipInputs:true});
    });
    el.budgetMaxInput.addEventListener("input", function(){
      var lo = state.minBudget===null ? BUDGET_MIN : state.minBudget;
      var hi = Math.max(typedBudget(el.budgetMaxInput, BUDGET_MAX), lo);
      setBudgetRange(lo, hi, {skipInputs:true});
    });
    // Leaving the field (or pressing Enter) writes the normalised value back.
    el.budgetMinInput.addEventListener("change", function(){ syncBudgetUI(); });
    el.budgetMaxInput.addEventListener("change", function(){ syncBudgetUI(); });
    syncBudgetUI();
  }

  function renderDaysChips(){
    el.daysChips.innerHTML = "";
    DAY_OPTIONS.forEach(function(v){
      var b = document.createElement("button");
      b.type="button"; b.className="chip gold"; b.textContent = v + " " + dayWord(v);
      b.setAttribute("aria-pressed", state.maxDays===v ? "true":"false");
      b.addEventListener("click", function(){ state.maxDays=v; renderDaysChips(); applyFilters(); });
      el.daysChips.appendChild(b);
    });
  }
  function dayWord(n){
    if (lang === "en") return n === 1 ? "day" : "days";
    if (n===1) return "день";
    if ([2,3,4].indexOf(n)!==-1) return "дня";
    return "дней";
  }

  function renderSourceChips(){
    el.sourceChips.innerHTML = "";
    SOURCES.forEach(function(s){
      var b = document.createElement("button");
      b.type="button"; b.className="chip"; b.disabled = !s.active;
      b.innerHTML = '<span class="dot" style="background:'+s.color+'"></span>' + sourceLabel(s) + (s.active ? "" : " " + t("soon"));
      b.setAttribute("aria-pressed", (s.active && state.sources.has(s.key)) ? "true":"false");
      if (s.active){
        b.addEventListener("click", function(){
          if (state.sources.has(s.key)) state.sources.delete(s.key); else state.sources.add(s.key);
          renderSourceChips(); applyFilters();
        });
      }
      el.sourceChips.appendChild(b);
    });
  }

  function renderTypeChips(){
    el.typeChips.innerHTML = "";
    var allBtn = document.createElement("button");
    allBtn.type="button"; allBtn.className="chip"; allBtn.textContent=t("all");
    allBtn.setAttribute("aria-pressed", state.type===null ? "true":"false");
    allBtn.addEventListener("click", function(){ state.type=null; renderTypeChips(); applyFilters(); });
    el.typeChips.appendChild(allBtn);
    // Only the types belonging to the selected kind: showing "Warehouse" while
    // the user is browsing housing is noise, and vice versa.
    var typesForKind = state.kind === "commercial" ? COMMERCIAL_TYPES
                     : state.kind === "residential" ? RESIDENTIAL_TYPES
                     : TYPE_OPTIONS;
    // NB: the loop variable must not be named `t` -- that would shadow the
    // t() translation helper inside this closure.
    typesForKind.forEach(function(tp){
      var b = document.createElement("button");
      b.type="button"; b.className="chip"; b.textContent=typeName(tp);
      b.setAttribute("aria-pressed", state.type===tp ? "true":"false");
      b.addEventListener("click", function(){ state.type = (state.type===tp) ? null : tp; renderTypeChips(); applyFilters(); });
      el.typeChips.appendChild(b);
    });
  }

  function setKind(kind){
    if (state.kind === kind) return;
    state.kind = kind;
    // A type from the other kind would silently match nothing.
    if (state.type && kindOf({type: state.type}) !== kind) state.type = null;
    BUDGET_MAX = (kind === "commercial") ? BUDGET_MAX_COMMERCIAL : BUDGET_MAX_RESIDENTIAL;
    // Any ceiling-relative budget must be reinterpreted against the new range,
    // otherwise "up to 45" silently becomes a hard filter on a 300-wide scale.
    state.minBudget = null; state.maxBudget = null;
    var tg = document.getElementById("kind-toggle");
    if (tg){
      Array.prototype.forEach.call(tg.querySelectorAll("button"), function(b){
        b.classList.toggle("active", b.getAttribute("data-kind") === kind);
      });
    }
    syncBudgetUI(); renderBudgetChips(); renderTypeChips(); renderComplexFilter(); applyFilters();
  }

  var kindToggleEl = document.getElementById("kind-toggle");
  if (kindToggleEl){
    kindToggleEl.addEventListener("click", function(e){
      var btn = e.target.closest("button[data-kind]");
      if (!btn) return;
      var kind = btn.getAttribute("data-kind");
      // Per-city pages hold one kind each: the other kind is a sibling page.
      if (PAGE){ if (kind !== PAGE.kind) location.href = pageHref(PAGE.city, kind); return; }
      setKind(kind);
    });
  }

  el.sortToggle.addEventListener("click", function(e){
    var btn = e.target.closest("button[data-sort]");
    if (!btn) return;
    state.sort = btn.getAttribute("data-sort");
    Array.prototype.forEach.call(el.sortToggle.querySelectorAll("button"), function(b){ b.classList.toggle("active", b===btn); });
    applyFilters();
  });

  el.perM2Toggle.addEventListener("change", function(){
    state.perM2 = el.perM2Toggle.checked;
    applyFilters();
  });

  el.poiSortSelect.addEventListener("change", function(){
    state.poiSort = el.poiSortSelect.value;
    applyFilters();
  });

  el.complexSelect.addEventListener("change", function(){
    state.complex = el.complexSelect.value || null;
    applyFilters();
  });

  function detailsHtml(l){
    if (!l.details) return "";
    var rows = DETAIL_ORDER.filter(function(k){ return l.details[k]; }).map(function(k){
      return '<div class="details-row"><dt>' + t("detailLabels")[k] + '</dt><dd>' + l.details[k] + '</dd></div>';
    }).join("");
    var open = state.openDetails.has(l.id);
    return '<button class="details-toggle" type="button" data-details-for="'+l.id+'" aria-expanded="'+open+'">' + t("detailsToggle") + ' <span class="arrow">▾</span></button>' +
      '<dl class="details-panel"' + (open ? "" : " hidden") + ' id="details-'+l.id+'">' + rows + '</dl>';
  }

  function applyFilters(){
    var city = CITIES[state.city];
    var list = LISTINGS.filter(function(l){
      if (l.city !== state.city) return false;
      if (l.details && l.details.duplicateOf) return false;
      if (!state.sources.has(l.source)) return false;
      if (state.district && l.district !== state.district) return false;
      if (state.complex && l.complex !== state.complex) return false;
      if (state.minBudget !== null && l.price < state.minBudget*1000000) return false;
      if (state.maxBudget !== null && l.price > state.maxBudget*1000000) return false;
      if (l.daysAgo > state.maxDays) return false;
      if (state.kind && kindOf(l) !== state.kind) return false;
      if (state.type && l.type !== state.type) return false;
      if (state.textSearch && listingSearchText(l).indexOf(state.textSearch) === -1) return false;
      if (state.showFavoritesOnly && !favorites.has(l.id)) return false;
      return true;
    });
    if (state.poiSort){
      list.forEach(function(l){ l._poiDist = nearestPoiKm(l, state.poiSort); });
      list.sort(function(a,b){
        if (a._poiDist===null && b._poiDist===null) return 0;
        if (a._poiDist===null) return 1;
        if (b._poiDist===null) return -1;
        return a._poiDist - b._poiDist;
      });
    } else if (state.perM2 && state.sort !== "new"){
      list.forEach(function(l){ l._perM2 = pricePerM2(l); });
      list.sort(function(a,b){
        if (a._perM2===null && b._perM2===null) return 0;
        if (a._perM2===null) return 1;
        if (b._perM2===null) return -1;
        return state.sort==="asc" ? a._perM2-b._perM2 : b._perM2-a._perM2;
      });
    } else {
      list.sort(function(a,b){
        if (a.price===null && b.price===null) return 0;
        if (a.price===null) return 1;
        if (b.price===null) return -1;
        if (state.sort==="new") return a.daysAgo-b.daysAgo || a.price-b.price;
        return state.sort==="asc" ? a.price-b.price : b.price-a.price;
      });
    }

    el.resultsCount.textContent = list.length + " " + declineObjav(list.length);
    var distLabel = state.district ? districtByKey(state.city, state.district).name : t("anyDistrict");
    var budgetLabel;
    if (state.minBudget===null && state.maxBudget===null) budgetLabel = t("anyBudget");
    else if (state.minBudget===null) budgetLabel = t("upTo") + " " + fmtPrice(state.maxBudget*1000000) + " " + t("perMonth");
    else if (state.maxBudget===null) budgetLabel = t("from") + " " + fmtPrice(state.minBudget*1000000) + " " + t("perMonth");
    else budgetLabel = t("from") + " " + fmtPrice(state.minBudget*1000000) + " " + t("to") + " " + fmtPrice(state.maxBudget*1000000) + " " + t("perMonth");
    var typeLabel = state.type ? typeName(state.type).toLowerCase() : t("anyType");
    var searchLabel = state.textSearch ? (' · ' + t("searchCtx") + ': "' + state.textSearch + '"') : "";
    var complexLabel = state.complex ? (" · " + t("complexCtx") + " " + state.complex) : "";
    el.resultsContext.textContent = cityName(city) + " · " + distLabel + complexLabel + " · " + typeLabel + " · " + budgetLabel + " · " + t("forDays") + " " + state.maxDays + " " + dayWord(state.maxDays) + searchLabel;

    el.resultsList.innerHTML = "";
    el.emptyState.hidden = list.length !== 0;

    list.forEach(function(l){
      var d = districtByKey(l.city, l.district);
      var src = SOURCE_LABEL[l.source];
      var card = document.createElement("article");
      card.className = "listing-card";
      var noticeHtml = (l.details && l.details.notice && l.details.notice.indexOf("⚠")===0)
        ? '<p class="listing-notice">' + noticeText(l.details) + '</p>' : "";
      var photos = l.details && l.details.photos;
      var photoHtml = (photos && photos.length)
        ? '<div class="listing-photos">' + photos.map(function(p, i){
            return '<img class="listing-photo" data-idx="' + i + '" src="' + p + '" alt="" loading="lazy" onerror="this.remove()">';
          }).join('') + '</div>'
        : "";
      var alsoOn = l.details && l.details.alsoOn;
      var alsoOnHtml = (alsoOn && alsoOn.length)
        ? '<p class="listing-also">' + t("alsoOn") + ' ' + alsoOn.map(function(a){
            var s = SOURCE_LABEL[a.source];
            return '<a href="' + a.url + '" target="_blank" rel="noopener">' + (s ? s.short : a.source) + '</a>';
          }).join(', ') + '</p>'
        : "";
      var priceHistory = l.details && l.details.priceHistory;
      var priceChangeHtml = "";
      if (priceHistory && priceHistory.length && l.price !== null){
        var prevPrice = priceHistory[priceHistory.length-1].price;
        if (prevPrice !== l.price){
          var down = l.price < prevPrice;
          priceChangeHtml = '<span class="price-change ' + (down?"down":"up") + '">' + (down?"↓":"↑") +
            ' ' + t("wasPrice") + ' ' + fmtPrice(prevPrice) + ' ₫</span>';
        }
      }
      var perM2Val = pricePerM2(l);
      var perM2Html = perM2Val ? ('<span class="price-per-m2">' + fmtPricePerM2(perM2Val) + '</span>') : "";
      card.innerHTML =
        photoHtml +
        '<div class="listing-top">' +
          '<span class="source-pill"><i style="background:'+src.color+'"></i>' + src.short + '</span>' +
          '<span class="listing-top-right">' +
            '<span class="posted">' + postedText(l) + '</span>' +
            '<button class="fav-btn" type="button" data-fav-id="' + l.id + '" aria-label="' + t("addFav") + '" aria-pressed="' + favorites.has(l.id) + '">' + (favorites.has(l.id) ? "★" : "☆") + '</button>' +
          '</span>' +
        '</div>' +
        '<div>' +
          '<div class="listing-type">' + typeName(l.type) + '</div>' +
          '<div class="listing-meta">' + d.name + (l.area ? (" · " + l.area + " " + t("m2")) : "") +
            (state.poiSort && l._poiDist!=null ? (' · <span class="poi-dist-badge">' + POI_STYLE[state.poiSort].icon + " " + fmtDist(l._poiDist) + '</span>') : "") +
            (l.complex ? ('<br><span class="complex-pill">🏢 ' + l.complex + '</span>') : "") +
          '</div>' +
        '</div>' +
        '<p class="listing-desc">' + descText(l) + '</p>' +
        noticeHtml +
        alsoOnHtml +
        detailsHtml(l) +
        '<div class="listing-bottom">' +
          '<span><span class="price">' + (l.price===null ? t("priceOnRequest") : (fmtPrice(l.price) + ' <small>' + t("perMonth") + '</small>')) + '</span>' + perM2Html + priceChangeHtml + '</span>' +
          '<a class="open-link" href="' + l.url + '" target="_blank" rel="noopener">' + t("openListing") + '</a>' +
        '</div>';
      var favBtn = card.querySelector(".fav-btn");
      favBtn.addEventListener("click", function(){
        toggleFavorite(l.id);
        var isFav = favorites.has(l.id);
        favBtn.setAttribute("aria-pressed", isFav);
        favBtn.textContent = isFav ? "★" : "☆";
        if (state.showFavoritesOnly && !isFav) applyFilters();
      });
      var toggleBtn = card.querySelector(".details-toggle");
      if (toggleBtn){
        toggleBtn.addEventListener("click", function(){
          var panel = card.querySelector(".details-panel");
          var willOpen = panel.hasAttribute("hidden");
          if (willOpen){ panel.removeAttribute("hidden"); state.openDetails.add(l.id); }
          else { panel.setAttribute("hidden",""); state.openDetails.delete(l.id); }
          toggleBtn.setAttribute("aria-expanded", willOpen);
        });
      }
      if (photos && photos.length){
        card.querySelectorAll(".listing-photo").forEach(function(img){
          img.addEventListener("click", function(){
            openLightbox(photos, Number(img.getAttribute("data-idx")));
          });
        });
      }
      el.resultsList.appendChild(card);
    });
    renderLeafletMarkers(list);
  }

  function declineObjav(n){
    if (lang === "en") return n === 1 ? "listing" : "listings";
    var mod10 = n%10, mod100 = n%100;
    if (mod10===1 && mod100!==11) return "объявление";
    if ([2,3,4].indexOf(mod10)!==-1 && (mod100<10 || mod100>=20)) return "объявления";
    return "объявлений";
  }

  el.resetBtn.addEventListener("click", function(){
    state.district = null; state.complex=null; state.minBudget=null; state.maxBudget=null; state.maxDays=14; state.sort="asc"; state.type=null; state.poiSort=""; state.textSearch=""; state.showFavoritesOnly=false; state.perM2=false
    // Reset returns to housing, so the budget ceiling must come back with it --
    // otherwise the slider keeps the 300M commercial scale on residential data.
    // On a per-city page the kind is the page itself and stays.
    state.kind = PAGE ? PAGE.kind : "residential";
    BUDGET_MAX = (state.kind === "commercial") ? BUDGET_MAX_COMMERCIAL : BUDGET_MAX_RESIDENTIAL;
    var kt = document.getElementById("kind-toggle");
    if (kt){ Array.prototype.forEach.call(kt.querySelectorAll("button"), function(b){
      b.classList.toggle("active", b.getAttribute("data-kind")===state.kind); }); }
    state.sources = new Set(SOURCES.filter(function(s){ return s.active; }).map(function(s){ return s.key; }));
    el.districtInput.value=""; el.poiSortSelect.value=""; el.textSearchInput.value=""; el.perM2Toggle.checked=false;
    el.favFilterToggle.setAttribute("aria-pressed","false"); el.favFilterToggle.textContent="☆ " + t("favFilter");
    Array.prototype.forEach.call(el.sortToggle.querySelectorAll("button"), function(b){ b.classList.toggle("active", b.getAttribute("data-sort")==="asc"); });
    syncBudgetUI(); renderBudgetChips(); renderDaysChips(); renderSourceChips(); renderTypeChips(); renderComplexFilter(); renderCityMap(); applyFilters();
  });

  var lightboxPhotos = [], lightboxIndex = 0;
  var lightboxEl = document.getElementById("lightbox");
  var lightboxMain = document.getElementById("lightbox-main");
  var lightboxThumbs = document.getElementById("lightbox-thumbs");

  function renderLightbox(){
    lightboxMain.src = lightboxPhotos[lightboxIndex];
    lightboxThumbs.innerHTML = "";
    if (lightboxPhotos.length > 1){
      lightboxPhotos.forEach(function(p, i){
        var t = document.createElement("img");
        t.src = p;
        t.loading = "lazy";
        t.className = (i === lightboxIndex) ? "active" : "";
        t.addEventListener("click", function(){ lightboxIndex = i; renderLightbox(); });
        lightboxThumbs.appendChild(t);
      });
    }
  }

  function openLightbox(photos, index){
    lightboxPhotos = photos; lightboxIndex = index;
    renderLightbox();
    lightboxEl.removeAttribute("hidden");
  }

  function closeLightbox(){ lightboxEl.setAttribute("hidden", ""); }

  function lightboxStep(delta){
    lightboxIndex = (lightboxIndex + delta + lightboxPhotos.length) % lightboxPhotos.length;
    renderLightbox();
  }

  document.getElementById("lightbox-close").addEventListener("click", closeLightbox);
  document.getElementById("lightbox-prev").addEventListener("click", function(){ lightboxStep(-1); });
  document.getElementById("lightbox-next").addEventListener("click", function(){ lightboxStep(1); });
  lightboxEl.addEventListener("click", function(e){ if (e.target === lightboxEl) closeLightbox(); });
  document.addEventListener("keydown", function(e){
    if (lightboxEl.hasAttribute("hidden")) return;
    if (e.key === "Escape") closeLightbox();
    else if (e.key === "ArrowLeft") lightboxStep(-1);
    else if (e.key === "ArrowRight") lightboxStep(1);
  });

  var copyAddrBtn = document.getElementById("copy-addr");
  if (copyAddrBtn){
    copyAddrBtn.addEventListener("click", function(){
      var addr = document.getElementById("usdt-addr").textContent.trim();
      var done = function(){
        copyAddrBtn.textContent = t("copied");
        setTimeout(function(){ copyAddrBtn.textContent = t("copy"); }, 1800);
      };
      // Copying a wallet address must never silently no-op. If the clipboard
      // API is unavailable, or its promise is rejected -- no user gesture,
      // permission denied, sandboxed frame -- fall back to execCommand, and
      // if that fails too, select the address so it can be copied by hand.
      var legacyCopy = function(){
        var ta = document.createElement("textarea");
        ta.value = addr; ta.setAttribute("readonly", "");
        ta.style.position = "fixed"; ta.style.opacity = "0";
        document.body.appendChild(ta); ta.select();
        var ok = false;
        try { ok = document.execCommand("copy"); } catch (e) { ok = false; }
        document.body.removeChild(ta);
        if (ok) { done(); return; }
        var node = document.getElementById("usdt-addr");
        var sel = window.getSelection(), range = document.createRange();
        range.selectNodeContents(node); sel.removeAllRanges(); sel.addRange(range);
        copyAddrBtn.textContent = t("selected");
        setTimeout(function(){ copyAddrBtn.textContent = t("copy"); }, 2600);
      };
      if (navigator.clipboard && window.isSecureContext){
        navigator.clipboard.writeText(addr).then(done, legacyCopy);
      } else {
        legacyCopy();
      }
    });
  }

  if (PAGE && PAGE.kind === "commercial"){
    // A commercial page starts on the commercial budget scale and with the
    // toggle showing which page this is; setKind() is never called here.
    BUDGET_MAX = BUDGET_MAX_COMMERCIAL;
    if (kindToggleEl){ Array.prototype.forEach.call(kindToggleEl.querySelectorAll("button"), function(b){
      b.classList.toggle("active", b.getAttribute("data-kind") === "commercial"); }); }
  }
  initTheme();
  initLeafletMap();
  renderCityTabs(); renderCityMap(); updatePoiSortAvailability(); setupBudgetSlider(); renderBudgetChips(); renderDaysChips(); renderSourceChips(); renderTypeChips(); renderComplexFilter(); applyFilters();
  initLang();
})();