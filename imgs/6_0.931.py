d = DslBezier()

d.position_pen(1,3)
d.position_pen(2,2)
d.curve(Direction.NW, Orient.right, Length.short, Radius.medium)
d.straight_line(Direction.SE, Length.medium)
d.position_pen(3,2)
d.straight_line(Direction.S, Length.short)
d.straight_line(Direction.SE, Length.long)

d.end()
