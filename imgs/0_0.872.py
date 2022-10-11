d = DslBezier()

d.position_pen(2,0)
d.curve(Direction.SE, Orient.right, Length.short, Radius.medium)
d.curve(Direction.SE, Orient.right, Length.long, Radius.medium)
d.position_pen(0,0)
d.straight_line(Direction.NE, Length.long)
d.straight_line(Direction.NW, Length.short)

d.end()
