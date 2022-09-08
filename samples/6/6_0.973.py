d = DslBezier()

d.position_pen(2,1)
d.curve(Direction.SW, Orient.left, Length.short, Radius.medium)
d.straight_line(Direction.W, Length.medium)
d.straight_line(Direction.SE, Length.medium)
d.straight_line(Direction.S, Length.long)
d.position_pen(3,0)
d.position_pen(2,2)

d.end()
