d = DslBezier()

d.position_pen(1,2)
d.straight_line(Direction.SE, Length.long)
d.position_pen(0,1)
d.curve(Direction.S, Orient.right, Length.medium, Radius.medium)
d.straight_line(Direction.SW, Length.short)
d.straight_line(Direction.N, Length.medium)
d.position_pen(1,2)

d.end()
