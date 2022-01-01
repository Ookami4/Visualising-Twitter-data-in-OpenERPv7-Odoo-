from openerp.osv import osv,fields
import openerp

class model_negatifstatistic(osv.osv):
    _name="twitter.negatifstatistic"
    _columns={
        'vaccine':fields.char("Vaccine"),
        'effective':fields.integer("Effective")
    }
    def create(self, cr, uid, values, context=None):
        existing=self.search(cr,uid,[("effective",">=","0")],context=context)
        if existing:
            super(model_negatifstatistic, self).unlink(cr,uid,existing,context=context)
        data={'effective':len(self.pool.get("twitter.pfizer").search(cr,uid,[("polarite","<","0")],context=context)),"vaccine":"Pfizer"}
        data2={'effective':len(self.pool.get("twitter.johnson").search(cr,uid,[("polarite","<","0")],context=context)),"vaccine":"Johnson"}
        data3={'effective':len(self.pool.get("twitter.astrazenica").search(cr,uid,[("polarite","<","0")],context=context)),"vaccine":"Astrazeneca"}
        data4={'effective':len(self.pool.get("twitter.sinopharm").search(cr,uid,[("polarite","<","0")],context=context)),"vaccine":"Sinopharm"}
        out=super(model_negatifstatistic, self).create(cr, uid, data, context=context)
        out=super(model_negatifstatistic, self).create(cr, uid, data2, context=context)
        out=super(model_negatifstatistic, self).create(cr, uid, data3, context=context)
        out=super(model_negatifstatistic, self).create(cr, uid, data4, context=context)
        return out
model_negatifstatistic()