d = DslBezier()

d.position_pen(2,2)
d.position_pen(1,1)
d.straight_line(Direction.E, Length.long)
d.curve(Direction.S, Orient.right, Length.short, Radius.medium)
d.position_pen(2,0)

d.end()
