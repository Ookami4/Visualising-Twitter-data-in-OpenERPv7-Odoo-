from openerp.osv import osv,fields
import openerp

class model_sinostatistic(osv.osv):
    _name="twitter.sinostatistic"
    _columns={
        'name':fields.char("Type"),
        'effective':fields.integer("Effective")
    }
    def create(self, cr, uid, values, context=None):
        id=self.pool.get("twitter.sinopharm").search(cr,uid,[("polarite",">=","0")],limit=1,context=context)
        if id:
            obj=self.pool.get("twitter.sinopharm").browse(cr,uid,id[0],context=context)
        existing=self.search(cr,uid,[("effective",">=","0")],context=context)
        if existing:
            super(model_sinostatistic, self).unlink(cr,uid,existing,context=context)
        data={'effective':len(self.pool.get("twitter.sinopharm").search(cr,uid,[("polarite",">","0")],context=context)),"name":"Sentiment Positive"}
        data2={'effective':len(self.pool.get("twitter.sinopharm").search(cr,uid,[("polarite","<","0")],context=context)),"name":"Sentiment Negative"}
        data3={'effective':len(self.pool.get("twitter.sinopharm").search(cr,uid,[("polarite","=","0")],context=context)),"name":"Sentiment Neutre"}
        out=super(model_sinostatistic, self).create(cr, uid, data, context=context)
        out=super(model_sinostatistic, self).create(cr, uid, data2, context=context)
        out=super(model_sinostatistic, self).create(cr, uid, data3, context=context)
        return out
        
model_sinostatistic()