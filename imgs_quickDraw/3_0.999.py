d = DslBezier()

d.position_pen(2,0)
d.curve(Direction.SW, Orient.right, Length.short, Radius.medium)
d.position_pen(2,0)
d.straight_line(Direction.W, Length.long)
d.curve(Direction.W, Orient.right, Length.short, Radius.medium)

d.end()
