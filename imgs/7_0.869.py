d = DslBezier()

d.position_pen(0,1)
d.straight_line(Direction.NE, Length.medium)
d.position_pen(2,3)
d.straight_line(Direction.E, Length.long)
d.position_pen(1,0)
d.curve(Direction.SE, Orient.right, Length.short, Radius.medium)
d.curve(Direction.NE, Orient.right, Length.short, Radius.high)

d.end()
