d = DslBezier()

d.position_pen(0,3)
d.curve(Direction.SW, Orient.right, Length.short, Radius.medium)
d.straight_line(Direction.SW, Length.long)
d.position_pen(1,2)
d.curve(Direction.NW, Orient.right, Length.short, Radius.high)
d.straight_line(Direction.S, Length.medium)

d.end()
