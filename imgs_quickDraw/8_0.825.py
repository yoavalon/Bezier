d = DslBezier()

d.position_pen(2,0)
d.position_pen(2,2)
d.straight_line(Direction.NW, Length.medium)
d.curve(Direction.S, Orient.right, Length.medium, Radius.low)
d.position_pen(1,3)
d.curve(Direction.SW, Orient.right, Length.short, Radius.medium)

d.end()
